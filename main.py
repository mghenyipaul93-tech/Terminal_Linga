from cli.parser import setup_parser
from cli.commands import handle_explain, handle_transpile


def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.command == "explain":
        handle_explain(args)

    elif args.command == "transpile":
        handle_transpile(args)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()