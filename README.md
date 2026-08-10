<div align="center">

# Software: Python and Data Analytics

**A seminar contribution on Python as a platform for data mining and analytics**

Data Mining Seminar · Department of Informatics · Technical University of Munich (TUM)

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-Plotly-1f4e79?logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License: Educational](https://img.shields.io/badge/License-Educational-blue.svg)](#license)

</div>

---

## Overview

This repository accompanies the seminar paper **_Software: Python and Data Analytics_**.
It surveys why Python has become one of the most widely used languages for data mining and
examines the ecosystem of scientific libraries that make it practical for real analytical
work. Rather than treating the libraries in isolation, the paper — and the accompanying
demo — show how they compose into a single, iterative workflow spanning data preparation,
modeling, evaluation, and communication of results.

The core idea is a **pipeline** in which each stage is handled by a purpose-built library:

<div align="center">

`pandas` &nbsp;→&nbsp; `NumPy` &nbsp;→&nbsp; `SciPy` &nbsp;→&nbsp; `scikit-learn` &nbsp;→&nbsp; `Plotly` &nbsp;→&nbsp; `Dash`

</div>

| Stage | Library | Role in the workflow |
|-------|---------|----------------------|
| Data preparation | **pandas** | Loading, filtering, and reshaping tabular data |
| Numerical computing | **NumPy** | Vectorized array operations and transforms |
| Statistical analysis | **SciPy** | Hypothesis testing and scientific routines |
| Machine learning | **scikit-learn** | Model fitting and evaluation metrics |
| Visualization | **Plotly** | Interactive, publication-quality charts |
| Deployment | **Dash** | Turning the analysis into a live web app |

---

## Repository structure


| Path | Description |
|------|-------------|
| [`paper/`](paper/) | The full seminar paper. |
| [`presentation/`](presentation/) | Slides presented during the seminar session. |
| [`demo/`](demo/) | A runnable dashboard that demonstrates the pipeline end to end — see [`demo/README.md`](demo/README.md). |

---

## Interactive demo

The demo turns the paper's pipeline into something you can explore. Using the **Gapminder**
dataset (bundled with Plotly, no download required), it renders an interactive bubble chart
of life expectancy against GDP per capita and, for the current selection, recomputes a
linear regression (**R²**) and a Welch **t-test** live as you move the year slider or toggle
continents.

### Quick start

```bash
cd demo
pip install -r requirements.txt
python dash_demo.py
```

Then open <http://127.0.0.1:8050>. Full usage notes are in
[`demo/README.md`](demo/README.md).

---

## Abstract

Python has become one of the most widely used programming languages for data mining and
data analytics thanks to its readability, rapid development, and extensive ecosystem of
scientific libraries. The paper discusses how Python supports data mining by examining both
the language — its paradigms, syntax, and performance — and the libraries commonly used
throughout analytical workflows: NumPy for numerical computing, pandas for preprocessing,
SciPy for statistical analysis, scikit-learn for machine learning, and Plotly and Dash for
visualization and deployment. It further shows how these tools combine into an iterative
process of data preparation, modeling, evaluation, and result communication. While
interpreted execution introduces runtime overhead, much of it is offset by optimized
libraries implemented in lower-level languages, giving Python a practical balance of
productivity, ecosystem support, and performance for modern data mining.

---

## Author

**Adem Yahmadi**
Department of Informatics, Technical University of Munich
[adem.yahmadi@tum.de](mailto:adem.yahmadi@tum.de)

## License

This material is provided for educational purposes as part of the TUM Data Mining Seminar.