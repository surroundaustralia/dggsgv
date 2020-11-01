# -*- coding: utf-8 -*-

# from wkt import WktSemantics, WktParser
#
#
import json


class Validator:

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
        return "Line\tValid\tMessages\n" \
                "---\t---\t---\n" \
                "1\tTrue\t-\n" \
                "2\tFalse\tThe Geometry Type provided is not valid.\n" \
                "\t\tIt must be one of: POINT, MULTIPOINT, LINESTRING,\n" \
                "\t\tMULTILINESTRING, POLYGON, MULTIPOLYGON,\n" \
                "\t\tGEOMETRYCOLLECTION\n"


def validate():
    return Validator()
