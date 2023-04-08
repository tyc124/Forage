import pandas
from dash import Dash, html, dcc, Input, Output
from plotly.express import line


data = pandas.read_csv('cleaned.csv')
data = data.sort_values(by='date') #sort the data by date

colors = {
    'primary': '#FEDBFF',
    'secondary': '#D598EB',
    'font': '#522A61'
}

#Dash
dash_app = Dash(__name__)

def generate_figure(data):
    line_chart = line(data, x='date', y='sales', title='Pink Morsel Sales')
    line_chart.update_layout(
        plot_bgcolor = colors['secondary'],
        paper_bgcolor = colors['primary'],
        font_color = colors['font']
    )
    return line_chart

visualization = dcc.Graph(
    id='visualization', 
    figure=generate_figure(data)
)

header = html.H1(
    'Pink Morsel Visualizer',
    id='header',
    style={
    'background-color': colors['secondary'],
    'color': colors['font'],
    'boarder-radius': '20px'
    }
)

region_picker = dcc.RadioItems(
    ['north', 'east', 'south', 'west', 'all'],
    'north',
    id='region_picker',
    inline=True
)

region_picker_wrapper = html.Div(
    [
    region_picker
    ],
    style={
    'font-size': '150%'
    }
)


@dash_app.callback(
    Output(visualization, 'figure'),
    Input(region_picker, 'value')
)


def update_graph(region):
    if region == 'all':
        trimmed_data = data
    else:
        trimmed_data = data[data['region'] == region]

    figure = generate_figure(trimmed_data)
    return figure


dash_app.layout = html.Div(
    [
    header,
    visualization,
    region_picker_wrapper
    ],
    style={
    'textAlign': 'center',
    'background-color': colors['primary'],
    'boarder-radius': '20px'
    }
)

#this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()
