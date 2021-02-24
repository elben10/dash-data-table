import importlib
import os
from pathlib import Path

import dash_html_components as html

from docs.components.gallery import gallery
from docs.components.wrapper import wrapper

EXCLUDE_FILES = ["__init__.py"]


def example_lookup(example_path):
    return {
        "/" + get_basename(path): importlib.import_module(pythonize_path(path))
        for path in example_path.iterdir()
        if path.is_file() and path.name not in EXCLUDE_FILES
    }


def pythonize_path(path):
    return str(path)[:-3].replace("/", ".")


def get_basename(path):
    return os.path.splitext(path)[0]


EXAMPLE_PATH = Path("examples")
EXAMPLES = example_lookup(EXAMPLE_PATH)


def layout(ctx):
    path = ctx["pathname"]

    if path == "/examples":
        return wrapper(
            [
                html.Div(
                    gallery(
                        [
                            {"href": href, "title": library.TITLE, "description": library.DESCRIPTION}
                            for href, library in EXAMPLES.items()
                        ]
                    ),
                    className="pt-5",
                )
            ],
            ctx,
        )
    elif EXAMPLES.get(path):
        return wrapper(EXAMPLES[path].layout(ctx), ctx)
    return wrapper(html.H3("Couldn't find the specified example"), ctx)
