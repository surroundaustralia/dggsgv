# -*- coding: utf-8 -*-

# from wkt import WktSemantics, WktParser
#
#
import json
from tatsu.util import asjson
from tatsu.exceptions import FailedParse as WktFailedParse
from .wkt import WKTParser, WKTSemantics


WKT_GEOM_TYPE = [
    "POINT",
    "MULTIPOINT",
    "LINESTRING",
    "MULTILINESTRING",
    "POLYGON",
    "MULTIPOLYGON",
    "GEOMETRYCOLLECTION",
]


class Validator:
    def __init__(self, data):
        # split on newline for multiple geometries
        lines = data.split("\n")
        self.results = []
        for i, line in enumerate(lines):
            if line.startswith("<") or WKT_GEOM_TYPE:
                # this looks like a WKT value, so try using that validator
                parser = WKTParser()
                try:
                    ast = parser.parse(data, rule_name="well_known_text_representation", semantics=WKTSemantics())
                    self.results.append((i, True, None))
                except WktFailedParse as e:
                    self.results.append((i, False, str(e)))

    def results_as_turtle(self):
        r = """<a:> <a:> <a:> ."""
        return r

    def results_as_json(self):
        r = [
            {
                "Line": 1,
                "Valid": True,
                "Message": None
            },
            {
                "Line": 2,
                "Valid": False,
                "Message": "The Geometry Type provided is not valid. It must be one of: POINT, MULTIPOINT, LINESTRING, MULTILINESTRING, POLYGON, MULTIPOLYGON, GEOMETRYCOLLECTION"
            },
        ]
        return json.dumps(r, indent=4)

    def results_as_table(self):
        print(self.results)
        table_header = "Line\tValid\tMessages\n----\t-----\t--------\n"
        table_body = ""
        for r in self.results:
            table_body += "{}\t{}\t{}\n".format(r[0], r[1], r[2].replace("\n", "\n\t\t\t"))

        return table_header + table_body


def validate(data):
    return Validator(data)
