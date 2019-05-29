from typing import Dict, Any

OUTPUT_HEADER = """
try:
    from typing import TypedDict
except ImportError:
    from mypy_extensions import TypedDict
"""

def convert_schema(schema: Dict[str, Any]) -> str:
    """Convert a given JSON Schema object into a series of TypedHint classes.

    :param schema: The schema to convert
    :type schema: Dict[str, Any]
    :return: The converted schema
    :rtype: str
    """
    return OUTPUT_HEADER
