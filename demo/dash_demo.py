import webbrowser
from threading import Timer

import numpy as np
import plotly.express as px
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from dash import Dash, dcc, html, Input, Output

df = px.data.gapminder()
YEARS = sorted(df["year"].unique())
CONTINENTS = sorted(df["continent"].unique())


def fit_stats(dff):
    x = np.log10(dff["gdpPercap"].to_numpy()).reshape(-1, 1)
    y = dff["lifeExp"].to_numpy()

    model = LinearRegression().fit(x, y)
    r2 = r2_score(y, model.predict(x))

    median_gdp = np.median(dff["gdpPercap"])
    rich = dff.loc[dff["gdpPercap"] >= median_gdp, "lifeExp"]
    poor = dff.loc[dff["gdpPercap"] < median_gdp, "lifeExp"]
    t, p = stats.ttest_ind(rich, poor, equal_var=False)
    return r2, t, p, rich.mean(), poor.mean()


app = Dash(__name__)
app.title = "Python & Data Analytics - live demo"

app.layout = html.Div(
    style={"maxWidth": "980px", "margin": "0 auto",
           "fontFamily": "system-ui, sans-serif", "padding": "12px"},
    children=[
        html.H2("Gapminder: one dataset, the whole pipeline"),
        html.P("pandas  \u2192  NumPy  \u2192  SciPy  \u2192  scikit-learn  \u2192  Plotly  \u2192  Dash",
               style={"color": "#1f4e79", "fontWeight": "600"}),

        html.Label("Continents"),
        dcc.Checklist(
            id="continents",
            options=[{"label": " " + c, "value": c} for c in CONTINENTS],
            value=CONTINENTS,
            inline=True,
            style={"marginBottom": "10px"},
        ),

        html.Label("Year"),
        dcc.Slider(
            id="year",
            min=min(YEARS), max=max(YEARS), step=5, value=min(YEARS),
            marks={int(y): str(y) for y in YEARS},
        ),

        dcc.Graph(id="bubble"),

        html.Div(id="stats", style={
            "background": "#eef2f7", "borderRadius": "8px",
            "padding": "12px 16px", "fontSize": "15px"}),
    ],
)


@app.callback(
    Output("bubble", "figure"),
    Output("stats", "children"),
    Input("year", "value"),
    Input("continents", "value"),
)
def update(year, continents):
    dff = df[(df["year"] == year) & (df["continent"].isin(continents))]
    if len(dff) < 3:
        return px.scatter(title="Pick at least one continent"), "Not enough data."

    fig = px.scatter(
        dff, x="gdpPercap", y="lifeExp", size="pop", color="continent",
        hover_name="country", log_x=True, size_max=60,
        range_y=[25, 90],
        labels={"gdpPercap": "GDP per capita (log)", "lifeExp": "life expectancy"},
        title=f"Life expectancy vs GDP \u2014 {year}",
    )
    fig.update_layout(transition_duration=400, margin=dict(t=50, r=10, b=10, l=10))

    r2, t, p, rich_m, poor_m = fit_stats(dff)
    sig = "significant" if p < 0.05 else "not significant"
    stats_panel = [
        html.B("Live analysis for "), html.B(str(year)), html.Br(),
        f"scikit-learn  R\u00b2 (lifeExp ~ log GDP) = {r2:.3f}", html.Br(),
        f"SciPy t-test  rich vs poor half:  t = {t:.2f},  p = {p:.1e}  ({sig})",
        html.Br(),
        f"mean lifeExp \u2014 richer half: {rich_m:.1f}   poorer half: {poor_m:.1f}",
    ]
    return fig, stats_panel


def _open():
    webbrowser.open_new("http://127.0.0.1:8050")


if __name__ == "__main__":
    Timer(1.2, _open).start()
    app.run(debug=False, port=8050)
