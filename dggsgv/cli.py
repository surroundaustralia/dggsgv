# -*- coding: latin-1 -*-
#

# This file is the command line argument handler for the module. It is not used
# when dggsgv is called within Python code as a library

import sys
import argparse
from pathlib import Path
from dggsgv import __version__, validate


class ShowVersion(argparse.Action):
    def __init__(
        self,
        option_strings,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help=None,
    ):
        super(ShowVersion, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        sys.stderr.write("DGGSGV Version: " + str(__version__) + "\n")
        parser.exit()


parser = argparse.ArgumentParser(
    description="DGGSGV {} command line tool.".format(str(__version__))
)


def get_data_from_file_or_string(val):
    if Path(val).is_file():
        return open(val).read()
    else:
        return val


parser.add_argument(
    "geometry",
    metavar="GEOM_FILE_OR_STRING",
    type=get_data_from_file_or_string,
    help="Either a file or a string containing the geometry literal value to validate."
)


parser.add_argument(
    "-o",
    "--output",
    default="table",
    choices=("table", "json", "turtle"),
    help="Choose an output format: a text table, 'table', JSON, 'json' or RDF in the turtle format, 'turtle'.",
)


def main():
    args = parser.parse_args()

    data = get_data_from_file_or_string(args.geometry)

    v = validate(data)
    if args.output == "turtle":
        print(v.results_as_turtle())
    elif args.output == "json":
        print(v.results_as_json())
    else:
        print(v.results_as_table())


if __name__ == "__main__":
    main()
