# Automobile Sales Analysis — Coursera Graded Assignment

This project includes Part 1 (visualizations) and Part 2 (Dash dashboard).
Run `python data/generate_dataset.py` to generate `data/automobile_sales.csv`,
then run the scripts in `src/` and `app/` as described below.

## Quick start
```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python data/generate_dataset.py
python src/visualizations.py   # creates figures/ with PNGs and a folium HTML map
python app/dashboard.py        # starts dash app at http://127.0.0.1:8050
```
