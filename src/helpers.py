import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / 'data' / 'automobile_sales.csv'

def load_data(path=None):
    p = Path(path) if path else DATA
    df = pd.read_csv(p, parse_dates=['date'])
    # ensure year/month columns exist
    if 'year' not in df.columns:
        df['year'] = df['date'].dt.year
    if 'month' not in df.columns:
        df['month'] = df['date'].dt.month
    return df
