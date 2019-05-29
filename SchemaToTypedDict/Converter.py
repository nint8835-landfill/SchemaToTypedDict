from typing import Dict, Any
from io import StringIO

OUTPUT_HEADER = """\
try:
    from typing import TypedDict
except ImportError:
    from mypy_extensions import TypedDict

from typing import Optional, List
"""

TYPE_MAP = {
    None: Any,
    "string": "str",
    "integer": "int",
    "number": "float",
    "array": "List",
}

class Converter(object):

    _output: StringIO

    def __init__(self):
        self._output = StringIO()
        self._output.write(OUTPUT_HEADER)

    def convert_schema(self, schema: Dict[str, Any]):
        self._output.write(f"\n\nclass {schema.get('title', 'Untitled Schema').replace(' ', '')}(TypedDict):\n")
        for prop_name, prop_details in schema.get('properties', {}).items():
            type_hint = TYPE_MAP[prop_details.get("type", None)]
            if type_hint == "List":
                inner_type = TYPE_MAP[prop_details.get("items", {}).get("type", None)]
                type_hint = f"{type_hint}[{inner_type}]"
            if prop_name not in schema.get('required', []):
                type_hint = f"Optional[{type_hint}]"
            self._output.write(f"    {prop_name}: {type_hint}\n")
        return self._output

def convert_schema(schema: Dict[str, Any]) -> StringIO:
    """Convert a given JSON Schema object into a series of TypedHint classes.

    :param schema: The schema to convert
    :type schema: Dict[str, Any]
    :return: The converted schema
    :rtype: str
    """
    return Converter().convert_schema(schema)
