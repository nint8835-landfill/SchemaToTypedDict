import json
import sys
import shutil

import click
import requests

from . import convert_schema


@click.command()
@click.option("--file", default=None, help="JSON Schema file to convert.")
@click.option("--url", default=None, help="URL to JSON Schema to convert.")
@click.option("--output", default=None, help="Output file to write classes to.")
def convert(file, url, output):
    """Convert a JSON Schema into a series of TypedDict classes."""
    schema = None
    if file:
        with open(file, encoding="utf8") as f:
            schema = json.load(f)

    if url:
        schema = requests.get(url).json()

    if schema:
        result = convert_schema(schema)
        result.seek(0)

        if output:
            with open(output, "w", encoding="utf8") as f:
                shutil.copyfileobj(result, f)
        else:
            shutil.copyfileobj(result, sys.stdout)
    else:
        print("No schema specified.")
        sys.exit(1)
