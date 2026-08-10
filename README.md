# Software: Python and Data Analytics

Materials for the **Data Mining Seminar** at the Technical University of Munich (TUM),
Department of Informatics.

**Author:** Adem Yahmadi · [adem.yahmadi@tum.de](mailto:adem.yahmadi@tum.de)

This seminar contribution surveys how Python supports data mining and data analytics.
It looks at the language itself and at the core scientific libraries used across an
analytical workflow — NumPy, pandas, SciPy, scikit-learn, and Plotly/Dash — and shows
how they fit together through data preparation, modeling, evaluation, and communication
of results.

## Repository structure

| Path | Contents |
|------|----------|
| [`paper/`](paper/) | The seminar paper (PDF). |
| [`presentation/`](presentation/) | The presentation slides (PDF). |
| [`demo/`](demo/) | Interactive Dash application demonstrating the full pipeline. See [`demo/README.md`](demo/README.md). |

## The demo in one line

An interactive Gapminder dashboard that walks the same pipeline described in the paper —
`pandas → NumPy → SciPy → scikit-learn → Plotly → Dash` — recomputing a linear
regression and a t-test live as you move the year slider.

```bash
cd demo
pip install -r requirements.txt
python dash_demo.py
```

Then open <http://127.0.0.1:8050> (the app tries to open it automatically).
Full instructions are in [`demo/README.md`](demo/README.md).

## License

Provided for educational purposes as part of the TUM Data Mining Seminar.
