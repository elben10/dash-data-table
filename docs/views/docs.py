import json

from docs.components.doc import doc_generator
from docs.components.wrapper import wrapper

with open("dash_data_table/components/metadata.json") as f:
    metadata = json.load(f)


def layout(ctx):
    return wrapper(
        doc_generator(metadata, "src/components/DashDataTable.react.js"), ctx
    )
