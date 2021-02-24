import random

import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output
from dash_data_table import DashDataTable

TITLE = "Clicklable rows"
DESCRIPTION = "Shows which row was clicked or double clicked"
WEIGHT = 2

columns = [
    {"name": "ID", "selector": "id"},
    {"name": "Title", "selector": "title"},
    {"name": "Directior", "selector": "director"},
    {"name": "Runtime (m)", "selector": "runtime", "right": True},
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
            DashDataTable(
                id="clickedRowsTable", title="Table", columns=columns, data=rows,
            ),
            html.Div(id="clickedRowsContainer"),
        ]
    )


def init_callbacks(app):
    @app.callback(
        Output("clickedRowsContainer", "children"),
        Input("clickedRowsTable", "currentClickedRow"),
        Input("clickedRowsTable", "currentDoubleClickedRow"),
    )
    def update_container(clicked_row, double_clicked_row):
        if clicked_row and double_clicked_row:
            return [
                html.P(f"The last row that was clicked was id: {clicked_row}"),
                html.P(
                    f"The last row that was double clicked was {double_clicked_row}"
                ),
            ]
        elif clicked_row and not double_clicked_row:
            return [
                html.P(f"The last row that was clicked was id: {clicked_row}"),
                html.P("No row has been double clicked yet"),
            ]
        return "No row has been clicked or double clicked yet"


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

