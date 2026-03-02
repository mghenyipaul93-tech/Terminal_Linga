import argparse
from config import APP_NAME, VERSION


def setup_parser():

    parser = argparse.ArgumentParser(
        prog="linga",
        description="LingaTerminal - Multi Dialect Translation Engine"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{APP_NAME} {VERSION}"
    )

    subparsers = parser.add_subparsers(dest="command")

    explain = subparsers.add_parser(
        "explain",
        help="Explain terminal command"
    )

    explain.add_argument("--cmd", required=True)
    explain.add_argument("--lang", required=True)

    transpile = subparsers.add_parser(
        "transpile",
        help="Convert indigenous logic into code"
    )

    transpile.add_argument("--code", required=True)
    transpile.add_argument("--to", required=True)

    return parser