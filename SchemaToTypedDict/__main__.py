import json
import sys

import click
import requests

from . import convert_schema


@click.command()
@click.option("--file", default=None, help="JSON Schema file to convert.")
@click.option("--url", default=None, help="URL to JSON Schema to convert.")
def convert(file, url):
    """Convert a JSON Schema into a series of TypedDict classes."""
    schema = None
    if file:
        with open(file, encoding="utf8") as f:
            schema = json.load(f)

    if url:
        schema = requests.get(url).json()

    if schema:
        print(convert_schema(schema))
    else:
        print("No schema specified.")
        sys.exit(1)
