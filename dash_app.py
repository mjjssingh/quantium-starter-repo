
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

all_regions = ['north', 'south', 'east', 'west']
app = Dash(__name__)

app.layout = html.Div(
    [
    html.H1('Pink Morsels Sales Chart'),
    dcc.Graph(id="graph"),
    dcc.RadioItems(
        id= 'radio-items',
        options=[
            {'label': region.capitalize(), 'value': region} for region in (all_regions)
        ],
        value = 'north',
        style={
            'marginTop':'20px',
            'fontSize': '25px'
        }
    )
    ],
    style={
        'font': 'italic 1.2em "Fira Sans", serif',
        'padding': '0px 50px ',
        'textAlign': 'center',
        'color': '#5204BF'
    }
)


@app.callback(
    Output("graph", "figure"),
    Input("radio-items", 'value')
)
def display_graph(selected_region):
    df = pd.read_csv('output_formatted.csv')
    df=df[df.Region == selected_region]
    fig = px.line(df, x='Date', y='Sales', height=750, template='simple_white')
    fig.update_traces(line_color='#5204BF')
    return fig


app.run_server(debug=True)