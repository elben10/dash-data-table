from dash import Dash
from dash_data_table import DashDataTable

TITLE = "Complex cells"
DESCRIPTION = "Render buttons, icons, checkboxes, badgelists within a cell"
WEIGHT = 6

columns = [
    {"name": "Button", "selector": "button", "type": "button"},
    {"name": "Badge List", "selector": "badgelist", "type": "badgeList",},
    {"name": "Checkbox", "selector": "checkbox", "type": "checkbox"},
    {"name": "Icon", "selector": "icon", "type": "icon"},
    {"name": "Link", "selector": "link", "type": "link"},
]

rows = [
    {
        "button": {"href": "/", "text": "This is a button"},
        "badgelist": [
            {"href": "/", "text": "Badge 1"},
            {"href": "/", "text": "Badge 2", "color": "success"},
            {"href": "/", "text": "Badge 3", "color": "danger"},
        ],
        "checkbox": True,
        "icon": {"href": "/", "icon": "far fa-smile-wink fa-2x"},
        "link": {"href": "/", "text": "Home"},
    },
] * 10


def layout(ctx=None):
    return DashDataTable(title="Table", columns=columns, data=rows,)


def init_callbacks(app):
    pass


app = Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css",
    ],
    external_scripts=[
        "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js",
    ],
)

app.layout = layout()

if __name__ == "__main__":
    app.run_server()
