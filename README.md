<div align="center">

# 🚗 Automobile Sales Analysis
### Interactive and Static Analysis of Automobile Sales During Recessions

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Dash](https://img.shields.io/badge/Dash-0A0A0A?style=flat-square&logo=dash&logoColor=white)](https://dash.plotly.com/)

[Overview](#-overview) ·
[Visualizations](#-visualizations) ·
[Dashboard](#-dash-dashboard) ·
[Tech Stack](#-tech-stack) ·
[Getting Started](#-getting-started) ·
[Project Structure](#-project-structure) ·
[Future Improvements](#-future-improvements) ·

</div>

---

## 📌 Overview

**Automobile Sales Analysis** is a project designed to analyze historical automobile sales data across multiple recession periods and non-recession years.  
It provides **static visualizations** for detailed insights and an **interactive Plotly Dash dashboard** for user-driven exploration.

> 🎯 **Objective:** Understand the impact of recessions on automobile sales, visualize trends, and provide an interactive reporting tool.

---

## 📊 Visualizations — Part 1

Static charts and a Folium map are generated and saved in the `figures/` directory.

| # | Chart | Description |
|---|-------|-------------|
| 1 | Line Chart | Automobile sales fluctuation over years |
| 2 | Bar Chart | Sales by vehicle type during recessions |
| 3 | Seaborn Plot | GDP variation during recession vs non-recession |
| 4 | Bubble Chart | Seasonality effect on mean automobile sales |
| 5 | Scatter Plot | Consumer confidence vs automobile sales |
| 6 | Pie Chart | Advertising expenditure share during recessions |
| 7 | Bar Chart | Advertising spend by vehicle type (recession vs non-recession) |
| 8 | Line Chart | Unemployment rate effect on vehicle type sales |
| 9 | Folium Map | Automobile sales by city (choropleth) |

**Script:** `src/visualizations.py`

---

## 📈 Dash Dashboard — Part 2

Interactive dashboard implemented with Plotly Dash (`app/dashboard.py`).

### Recession Period Statistics
- Average automobile sales per year (line chart)
- Average sales by vehicle type (bar chart)
- Advertising expenditure share by vehicle type (pie chart)
- Unemployment rate effect on vehicle type sales (bar chart)

### Yearly Statistics *(select a year)*
- Monthly automobile sales (line chart)
- Sales per vehicle type per month (line chart)
- Average vehicles sold by type per year (bar chart)
- Advertising expenditure per vehicle type (pie chart)

---

## 🛠 Tech Stack

| Category | Libraries |
|----------|-----------|
| Data manipulation | `pandas`, `numpy` |
| Static visualizations | `matplotlib`, `seaborn` |
| Geospatial map | `folium` |
| Interactive charts | `plotly` |
| Web dashboard | `dash` |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager

### 1 — Clone the repository

```bash
git clone https://github.com/MehmetErtass/automobile-sales-analysis.git
cd automobile-sales-analysis
```

### 2 — Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Generate the dataset

```bash
python data/generate_dataset.py
```

> Creates `data/automobile_sales.csv` — used by both parts of the project.

### 5 — Run Part 1 (Static Visualizations)

```bash
python src/visualizations.py
```

> Output PNGs and the Folium HTML map will be saved in `figures/`.

### 6 — Run Part 2 (Interactive Dashboard)

```bash
python app/dashboard.py
```

> Open **http://127.0.0.1:8050** in your browser.

---

## 📁 Project Structure

```
automobile-sales-analysis/
│
├── app/
│   └── dashboard.py          # Plotly Dash application
│
├── data/
│   └── generate_dataset.py   # Synthetic dataset generator → automobile_sales.csv
│
├── figures/                  # Auto-generated outputs
│   ├── *.png                 # Static charts
│   └── *.html                # Folium interactive map
│
├── src/
│   └── visualizations.py     # Static visualization scripts
│
├── requirements.txt          # Project dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Add time-series forecasting for post-recession recovery trends
- [ ] Integrate real-world dataset (e.g. FRED, BLS) to replace synthetic data
- [ ] Add vehicle-type-level drill-down filters to the dashboard
- [ ] Deploy dashboard online (Render / Railway / Hugging Face Spaces)
- [ ] Export dashboard charts as PDF reports

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Mehmet Ertaş**  
[![GitHub](https://img.shields.io/badge/GitHub-MehmetErtass-181717?style=flat-square&logo=github)](https://github.com/MehmetErtass)

*Made with ❤️ by Mehmet Ertaş*

</div>
