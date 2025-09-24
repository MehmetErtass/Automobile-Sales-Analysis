"""Generates a synthetic automobile sales dataset used by the project."""
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent
np.random.seed(42)

years = list(range(2005, 2021))
months = list(range(1,13))
vehicle_types = ['Sedan', 'SUV', 'Truck', 'Coupe']

rows = []
for y in years:
    recession = 1 if (2008 <= y <= 2009) or (y == 2020) else 0
    for m in months:
        for vt in vehicle_types:
            base = 2000 if vt=='Sedan' else 1800 if vt=='SUV' else 1000 if vt=='Truck' else 700
            season_factor = 1.2 if m in [5,6,7,8,9] else 0.9
            recession_factor = 0.7 if recession else 1.05
            noise = np.random.normal(0, base*0.05)
            sales = max(0, int((base * season_factor * recession_factor) + noise))
            avg_price = int((20000 + (1000 if vt=='SUV' else 0) + (500 if vt=='Truck' else 0)) * (1 + np.random.normal(0,0.03)))
            adv = int(50000 * (1.2 if recession else 1.0) * (1 + np.random.normal(0,0.15)))
            gdp = 15000 + (y-2005)*50 + np.random.normal(0,200)
            unemployment = 6.0 + (0.5 if recession else -0.1) + np.random.normal(0,0.5)
            lat = 40.0 + np.random.normal(0,0.5)
            lon = -74.0 + np.random.normal(0,0.5)
            rows.append({
                'year': y,
                'month': m,
                'date': f"{y}-{m:02d}-01",
                'vehicle_type': vt,
                'sales_volume': sales,
                'avg_price': avg_price,
                'advertising_expenditure': adv,
                'gdp': gdp,
                'unemployment_rate': unemployment,
                'recession': recession,
                'latitude': lat,
                'longitude': lon
            })

df = pd.DataFrame(rows)
OUT.joinpath('automobile_sales.csv').write_text(df.to_csv(index=False))
print('Generated', OUT.joinpath('automobile_sales.csv'))
