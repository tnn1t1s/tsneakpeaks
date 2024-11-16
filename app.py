from dash import Dash, html, dcc, callback, Output, Input
from tsneakpeaks import TSneakPeaks
import plotly.graph_objects as go
from pathlib import Path

app = Dash(__name__)

# Load data
peaks = TSneakPeaks("test_data")
peaks.load_data()
fig = peaks.visualize()

# Get just filenames
image_names = [Path(p).name for p in peaks.image_paths]

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='3d-plot', figure=fig)
    ], style={'width': '70%', 'float': 'left'}),
    
    html.Div([
        html.Img(id='selected-image', style={'width': '100%'}),
        html.Div(id='click-data')  # Added this
    ], style={'width': '30%', 'float': 'right'})
])

@callback(
    [Output('selected-image', 'src'),
     Output('click-data', 'children')],
    Input('3d-plot', 'clickData')
)
def display_image(clickData):
    if not clickData:
        return '', 'No click data'
    point_index = clickData['points'][0]['pointNumber']
    return f'/assets/{image_names[point_index]}', str(clickData)

if __name__ == '__main__':
    app.run(debug=True)
