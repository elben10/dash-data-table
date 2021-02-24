from dash import Dash
from dash_data_table import DashDataTable


# Basic test for the component rendering.
# The dash_duo pytest fixture is installed with dash (v1.0+)
def test_render_component(dash_duo):
    # Start a dash app contained as the variable `app` in `usage.py`
    app = Dash()
    app.layout = DashDataTable(columns=[])
    dash_duo.start_server(app)
