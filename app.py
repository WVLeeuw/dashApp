import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Hello Dash!'),
    dcc.Dropdown(id='dropdown',
                 options=[
                     {'label': 'boats', 'value': 'boats'},
                     {'label': 'cars', 'value': 'cars'}
                 ],
                 value=[],
                 multi=True
                 ),
    html.Div(id='my-div'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_selection(value):

    if value == ['cars']:
        return dcc.Graph(
            id='example',
            figure={
                'data': [{'x': [1, 2, 3, 4, 5], 'y': [8, 6, 4, 6, 8], 'type': 'bar', 'name': 'cars'}
                         ],
                'layout': {
                    'title': 'example graph'
                }
            })

    if value == ['boats']:
        return dcc.Graph(
            id='example',
            figure={
                'data': [{'x': [1, 2, 3, 4, 5], 'y': [5, 3, 7, 2, 1], 'type': 'line', 'name': 'boats'}
                         ],
                'layout': {
                    'title': 'example graph'
                }
            })

    if value == ['boats', 'cars']:
        return dcc.Graph(
            id='example',
            figure={
                'data': [{'x': [1, 2, 3, 4, 5], 'y': [8, 6, 4, 6, 8], 'type': 'bar', 'name': 'cars'},
                         {'x': [1, 2, 3, 4, 5], 'y': [5, 3, 7, 2, 1], 'type': 'line', 'name': 'boats'}
                         ],
                'layout': {
                    'title': 'example graph'
                }
            })


if __name__ == '__main__':
    app.run_server(debug=True)
