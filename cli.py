from pathlib import Path
from shutil import copy, rmtree
from typing import List, Union

import typer

app = typer.Typer()


@app.command()
def copy_files(
    path_in: Path,
    path_out: Path,
    create: bool = True,
    excluded: List[str] = typer.Option([]),
):
    if not path_out.exists() and create:
        path_out.mkdir()

    for file in path_in.iterdir():
        if file.is_file() and file.name not in excluded:
            copy(file, path_out / file.name)


@app.command()
def clean_folder(path: Path, excluded: List[str] = typer.Option([])):
    for file in path.iterdir():
        if file.is_file() and file.name not in excluded:
            file.unlink()


if __name__ == "__main__":
    app()
