import random

from dash import Dash
from dash_data_table import DashDataTable

columns = [
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


app = Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css",
    ],
)

app.layout = DashDataTable(title="Table", columns=columns, data=rows,)

if __name__ == "__main__":
    app.run_server(debug=True)
