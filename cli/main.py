"""Argparse CLI skeleton / Esqueleto de CLI com argparse."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli",
        description="Sample CLI / CLI de exemplo",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    greet = sub.add_parser("greet", help="Print a greeting / Imprime uma saudação")
    greet.add_argument("--name", default="world", help="Name to greet / Nome a saudar")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "greet":
        print(f"Hello, {args.name}!")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2
