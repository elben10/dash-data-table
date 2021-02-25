import random

from dash import Dash
from dash.dependencies import Input, Output
from dash_data_table import DashDataTable

TITLE = "Remote Sorting"
DESCRIPTION = "Enable remote sorting using python as backend"
WEIGHT = 4

ROWS = 37

columns = [
    {"name": "ID", "selector": "id", "sortable": True},
    {"name": "Title", "selector": "title"},
    {"name": "Directior", "selector": "director"},
    {"name": "Runtime (m)", "selector": "runtime", "right": True},
]

data = [
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
    for _ in range(ROWS)
]


def layout(ctx=None):
    return DashDataTable(
        id="remoteSortingTable",
        title="Table",
        columns=columns,
        persistTableHead=True,
        paginationServer=True,
        sortServer=True,
    )


def init_callbacks(app):
    @app.callback(
        Output("remoteSortingTable", "data"),
        Output("remoteSortingTable", "paginationTotalRows"),
        Input("remoteSortingTable", "currentPage"),
        Input("remoteSortingTable", "currentRowsPerPage"),
        Input("remoteSortingTable", "currentSorting"),
    )
    def update_table(page, rows_per_page, sorting):
        page = page if page else 1
        rows_per_page = rows_per_page if rows_per_page else 10
        if sorting:
            rows = sorted(data, key=lambda elem: elem[sorting["column"]])
            if sorting["sortDirection"] == "desc":
                rows = rows[::-1]
        else:
            rows = data
        return rows[(page - 1) * rows_per_page : page * rows_per_page], ROWS


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
