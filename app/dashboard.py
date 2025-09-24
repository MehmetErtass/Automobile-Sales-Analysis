"""Dash app for Part 2 of the assignment."""
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from src.helpers import load_data

app = dash.Dash(__name__)
app.title = 'Automobile Sales Recession Dashboard'

DF = load_data()

app.layout = html.Div([
    html.H1('Automobile Sales — Recession & Yearly Reports'),
    html.Div([
        html.Label('Select Vehicle Type'),
        dcc.Dropdown(id='vehicle-dropdown', options=[{'label':v,'value':v} for v in DF['vehicle_type'].unique()], value='Sedan')
    ], style={'width':'30%','display':'inline-block'}),

    html.Div([
        html.Label('Select Period'),
        dcc.Dropdown(id='period-dropdown', options=[{'label':'All','value':'All'},{'label':'Recession','value':1},{'label':'Non-Recession','value':0}], value='All')
    ], style={'width':'30%','display':'inline-block','marginLeft':'20px'}),

    html.Div(id='output-container', className='output-class', style={'marginTop':20}),

    dcc.Graph(id='recession-graph'),
    dcc.Graph(id='yearly-graph')
])

@app.callback(
    [Output('output-container','children'), Output('recession-graph','figure'), Output('yearly-graph','figure')],
    [Input('vehicle-dropdown','value'), Input('period-dropdown','value')]
)
def update_dashboard(vehicle, period):
    dff = DF.copy()
    if period in [0,1]:
        dff = dff[dff['recession']==int(period)]
    total_sales = int(dff[dff['vehicle_type']==vehicle]['sales_volume'].sum())
    avg_price = int(dff[dff['vehicle_type']==vehicle]['avg_price'].mean())
    text = html.Div([html.P(f'Total sales for {vehicle}: {total_sales}'), html.P(f'Average price: {avg_price}')])

    rec_df = dff[dff['vehicle_type']==vehicle].groupby('year', as_index=False)['sales_volume'].sum()
    fig_rec = px.bar(rec_df, x='year', y='sales_volume', title='Yearly Sales for Selected Vehicle')

    yearly = dff.groupby('year', as_index=False)['sales_volume'].sum()
    fig_year = px.line(yearly, x='year', y='sales_volume', title='Total Yearly Sales (Selected Period)')

    return text, fig_rec, fig_year

if __name__ == '__main__':
    app.run(debug=True, port=8050, host='127.0.0.1')

