from dash import Dash

app = Dash(
    __name__,
    external_scripts=[
        "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.min.js",
    ],
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css",

        "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.13.1/build/styles/monokai-sublime.min.css"
    ],
    suppress_callback_exceptions=True,
)
server = app.server
