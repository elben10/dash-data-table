import json
import random

import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output
from dash_data_table import DashDataTable

TITLE = "Sorting"
DESCRIPTION = "Enable column sorting"
WEIGHT = 1

columns = [
    {"name": "ID", "selector": "id", "sortable": True},
    {"name": "Title", "selector": "title", "sortable": True},
    {"name": "Directior", "selector": "director", "sortable": True},
    {"name": "Runtime (m)", "selector": "runtime", "sortable": True, "right": True},
]

rows = [
    {
        "id": random.randint(0, int(1e8)),
        "title": "Beetlejuice",
        "year": "1988",
        "runtime": "92",
        "genres": ["Comedy", "Fantasy"],
        "director": "Tim Burton",
        "actors": "Alec Baldwin, Geena Davis, Annie McEnroe, Maurice Page",
        "plot": 'A couple of recently deceased ghosts contract the services of a "bio-exorcist" in order to remove the obnoxious new owners of their house.',
        "posterUrl": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwODE3MDE0MV5BMl5BanBnXkFtZTgwNTk1MjI4MzE@._V1_SX300.jpg",
    }
    for _ in range(100)
]


def layout(ctx=None):
    return html.Div(
        [
            DashDataTable(id="sortingTable", title="Table", columns=columns, data=rows,),
            html.Div(id="sortingContainer"),
        ]
    )


def init_callbacks(app):
    @app.callback(Output("sortingContainer", "children"), Input("sortingTable", "currentSorting"))
    def update_container(sorting):
        if sorting:
            return json.dumps(sorting)
        return "No sorting"


app = Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css",
    ],
    external_scripts=[
        "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js",
    ],
)


if __name__ == "__main__":
    app.layout = layout()
    init_callbacks(app)
    app.run_server()

