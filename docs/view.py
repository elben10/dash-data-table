import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from docs.app import app, server
from docs.components.wrapper import wrapper
from docs.views import docs, examples, home

app.layout = html.Div([dcc.Location(id="location"), html.Div(id="content")])

ROUTES = [
    {"path": "/docs", "layout": docs.layout, "title": "Documentation", "navbar": True},
    {"path": "/examples", "layout": examples.layout, "title": "Examples", "navbar": True},
    {"path": "/", "layout": home.layout, "title": "Home", "navbar": False},
]

CONTEXT = {"title": "Dash Data Table", "routes": ROUTES}


@app.callback(Output("content", "children"), Input("location", "pathname"))
def route(pathname):
    for route in ROUTES:
        if pathname.startswith(route["path"]):
            context = {**CONTEXT, "pathname": pathname, **route.get("context", {})}
            return route["layout"](context)
    return wrapper(html.H1("404"))


if __name__ == "__main__":
    app.run_server(debug=True)
