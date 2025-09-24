"""Part 1 visualizations: saves PNGs into figures/ and a folium html map."""
import os
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import folium
from src.helpers import load_data
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

OUT = Path(__file__).parent.parent / 'figures'
OUT.mkdir(exist_ok=True)

def task_1_1_line_by_year(df):
    yearly = df.groupby('year', as_index=False)['sales_volume'].sum()
    plt.figure(figsize=(10,5))
    plt.plot(yearly['year'], yearly['sales_volume'], marker='o')
    plt.title('Automobile Sales — Yearly Trend')
    plt.xlabel('Year')
    plt.ylabel('Total Sales Volume')
    plt.grid(True)
    f = OUT / 'line_plot_1.png'
    plt.savefig(f, bbox_inches='tight')
    plt.close()

def task_1_2_lines_by_vehicle_type(df):
    yearly_type = df.groupby(['year','vehicle_type'])['sales_volume'].sum().reset_index()
    plt.figure(figsize=(11,6))
    for vt, grp in yearly_type.groupby('vehicle_type'):
        plt.plot(grp['year'], grp['sales_volume'], marker='o', label=vt)
    plt.title('Sales Trends by Vehicle Type')
    plt.xlabel('Year'); plt.ylabel('Sales Volume'); plt.legend(); plt.grid(True)
    f = OUT / 'line_by_type.png'
    plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_3_seaborn_compare_recession(df):
    df['period'] = df['recession'].map({1: 'Recession', 0: 'Non-Recession'})
    agg = df.groupby(['period','vehicle_type','year'])['sales_volume'].sum().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(data=agg, x='year', y='sales_volume', hue='vehicle_type', style='period', markers=True)
    plt.title('Sales trend per vehicle type — Recession vs Non-Recession')
    f = OUT / 'seaborn_recession_compare.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_4_subplots_gdp(df):
    df['period'] = df['recession'].map({1: 'Recession', 0: 'Non-Recession'})
    fig, axes = plt.subplots(1,2, figsize=(14,5), sharey=True)
    for ax, (period, grp) in zip(axes, df.groupby('period')):
        yearly_gdp = grp.groupby('year')['gdp'].mean().reset_index()
        ax.plot(yearly_gdp['year'], yearly_gdp['gdp'], marker='o')
        ax.set_title(f'GDP — {period}'); ax.set_xlabel('Year'); ax.set_ylabel('GDP'); ax.grid(True)
    plt.tight_layout(); f = OUT / 'gdp_recession_subplots.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_5_bubble_seasonality(df):
    monthly = df.groupby(['month'])['sales_volume'].agg(['mean','std']).reset_index()
    plt.figure(figsize=(10,6))
    plt.scatter(monthly['month'], monthly['mean'], s=(monthly['std']+1)*50, alpha=0.6)
    plt.title('Seasonality impact on Automobile Sales'); plt.xlabel('Month'); plt.ylabel('Average Sales Volume')
    f = OUT / 'bubble_seasonality.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_6_scatter_price_vs_sales_recession(df):
    rec = df[df['recession']==1].groupby(['vehicle_type','year'])[['avg_price','sales_volume']].mean().reset_index()
    plt.figure(figsize=(10,6))
    for vt, grp in rec.groupby('vehicle_type'):
        plt.scatter(grp['avg_price'], grp['sales_volume'], label=vt)
    plt.title('Price vs Sales Volume during Recession'); plt.xlabel('Average Price'); plt.ylabel('Sales Volume'); plt.legend()
    f = OUT / 'scatter_price_sales_recession.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_7_pie_ad_spend_recession_vs_non(df):
    df['period'] = df['recession'].map({1:'Recession',0:'Non-Recession'})
    agg = df.groupby('period', as_index=False)['advertising_expenditure'].sum()
    plt.figure(figsize=(6,6)); plt.pie(agg['advertising_expenditure'], labels=agg['period'], autopct='%1.1f%%')
    plt.title('Advertising expenditure — Recession vs Non-Recession'); f = OUT / 'pie_ad_recession_vs_non.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_8_pie_ad_by_type_recession(df):
    rec = df[df['recession']==1]
    agg = rec.groupby('vehicle_type', as_index=False)['advertising_expenditure'].sum()
    plt.figure(figsize=(6,6)); plt.pie(agg['advertising_expenditure'], labels=agg['vehicle_type'], autopct='%1.1f%%')
    plt.title('Advertising expenditure by vehicle type (Recession)'); f = OUT / 'pie_ad_by_type_recession.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def task_1_9_line_unemployment_effect(df):
    rec = df[df['recession']==1]
    agg = rec.groupby(['year','vehicle_type'])[['sales_volume','unemployment_rate']].mean().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(data=agg, x='year', y='sales_volume', hue='vehicle_type', marker='o')
    ax2 = plt.twinx()
    uni = rec.groupby('year')['unemployment_rate'].mean().reset_index()
    ax2.plot(uni['year'], uni['unemployment_rate'], linestyle='--', marker='x')
    ax2.set_ylabel('Unemployment Rate'); plt.title('Effect of Unemployment on Vehicle Type Sales (Recession)')
    f = OUT / 'line_unemployment_recession.png'; plt.savefig(f, bbox_inches='tight'); plt.close()

def create_folium_map(df):
    sample = df.sample(min(200, len(df)))
    m = folium.Map(location=[sample['latitude'].mean(), sample['longitude'].mean()], zoom_start=6)
    for _, r in sample.iterrows():
        folium.CircleMarker(location=[r['latitude'], r['longitude']], radius=max(2, int(r['sales_volume']/500)), popup=str(r['sales_volume']), fill=True).add_to(m)
    out = Path(__file__).parent.parent / 'figures' / 'sales_map.html'
    m.save(out)

if __name__ == '__main__':
    df = load_data()
    df['period'] = df['recession'].map({1:'Recession',0:'Non-Recession'})
    task_1_1_line_by_year(df); task_1_2_lines_by_vehicle_type(df); task_1_3_seaborn_compare_recession(df)
    task_1_4_subplots_gdp(df); task_1_5_bubble_seasonality(df); task_1_6_scatter_price_vs_sales_recession(df)
    task_1_7_pie_ad_spend_recession_vs_non(df); task_1_8_pie_ad_by_type_recession(df); task_1_9_line_unemployment_effect(df)
    create_folium_map(df)
