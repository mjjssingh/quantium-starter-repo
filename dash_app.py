from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

all_regions = ['north', 'south', 'east', 'west']

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsels Sales Chart'),

    # html.Button("Switch Axis", n_clicks=0,
    #             id='button'),
    dcc.Graph(id="graph"),
    dcc.RadioItems(
        id='radio-button',
        options=[
            {'label': region.capitalize(), 'value': region} for region in all_regions
        ],
        value='north',
        style={
            'marginTop': '20px',
            'color': '#ffffff'
        }
    )
],
    style={
        'backgroundColor': '#0B2740',
        'color': '#ffffff',
        'margin': 0,
        'padding': '20px 50px 30px',
        'textAlign': 'center',
        'fontSize': '20px',
        'font': 'italic 1.2em "Fira Sans", serif',
        'borderRadius':'50px'
    }

)


@app.callback(
    Output("graph", "figure"),
    Input('radio-button', 'value')
)
def display_graph(selected_region):
    df = pd.read_csv('output_formatted.csv')  # replace with your own data source
    df = df[df.Region == selected_region]
    color =['#C729F2', '#7B17A6', '#3B0E59', '#0B2740']
    fig = px.line(df, x='Date', y='Sales', height =700,template="simple_white")
    fig.update_traces(line_color=color[3])

    return fig


app.run_server(debug=True)
