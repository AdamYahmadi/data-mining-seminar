<div align="center">

# Live Demo — Python and Data Analytics

**An interactive dashboard that runs the seminar's analytical pipeline end to end**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-Plotly-1f4e79?logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Stats-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org/)

</div>

---

## Overview

This [Dash](https://dash.plotly.com/) application makes the paper's pipeline tangible: the
same sequence of libraries, wired together into a single interactive tool you can explore in
the browser.

<div align="center">

`pandas` &nbsp;→&nbsp; `NumPy` &nbsp;→&nbsp; `SciPy` &nbsp;→&nbsp; `scikit-learn` &nbsp;→&nbsp; `Plotly` &nbsp;→&nbsp; `Dash`

</div>

It uses the **Gapminder** dataset (bundled with Plotly — no download required). For the
selected year and continents, the app filters the data, fits a model, runs a statistical
test, and re-renders the chart and results together, live, on every interaction.

---

## What it does

| Step | Library | Action |
|------|---------|--------|
| Filter | **pandas** | Selects rows for the chosen year and continents |
| Transform | **NumPy** | Vectorized `log10` of GDP per capita |
| Model | **scikit-learn** | Fits `lifeExp ~ log10(GDP)` and reports **R²** |
| Test | **SciPy** | Welch **t-test** of life expectancy, richer vs. poorer half by GDP |
| Visualize | **Plotly** | Interactive bubble chart of life expectancy vs. GDP |
| Serve | **Dash** | Slider, checkboxes, and a live-updating results panel |

Everything recomputes the moment you move the year slider or toggle a continent.

---

## Requirements

- **Python 3.9** or newer
- The packages listed in [`requirements.txt`](requirements.txt)

---

## Setup and run

From this `demo/` directory:

```bash
# 1. (optional) create an isolated environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. install dependencies
pip install -r requirements.txt

# 3. launch the app
python dash_demo.py
```

The app starts a local server and tries to open your browser automatically. If it doesn't,
open <http://127.0.0.1:8050> manually. Press `Ctrl+C` in the terminal to stop it.