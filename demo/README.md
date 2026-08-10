# Live Demo — Python and Data Analytics

An interactive [Dash](https://dash.plotly.com/) application that runs the same analytical
pipeline described in the seminar paper, end to end and in real time:

```
pandas  →  NumPy  →  SciPy  →  scikit-learn  →  Plotly  →  Dash
```

## What it does

The app uses the **Gapminder** dataset (bundled with Plotly, no download needed). For the
selected year and continents it:

- draws an interactive bubble chart of **life expectancy vs. GDP per capita** (Plotly),
- fits a linear regression of `lifeExp ~ log10(GDP)` and reports its **R²** (scikit-learn),
- runs a **Welch t-test** comparing life expectancy of the richer vs. poorer half of
  countries by GDP (SciPy),

and recomputes all of it live as you move the year slider or toggle continents.

## Requirements

- Python 3.9 or newer
- The packages listed in [`requirements.txt`](requirements.txt)

## Setup and run

From this `demo/` directory:

```bash
# (optional) create an isolated environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python dash_demo.py
```

The app starts a local server and tries to open your browser automatically. If it doesn't,
open <http://127.0.0.1:8050> manually. Press `Ctrl+C` in the terminal to stop it.

## How to use it

- **Year slider** — pick a year (1952–2007) and watch the bubbles move.
- **Continent checkboxes** — filter which continents are included; the chart and the
  statistics below it update together.
- The panel under the chart shows the live R², t-test result, and the mean life expectancy
  of the richer and poorer halves for the current selection.
