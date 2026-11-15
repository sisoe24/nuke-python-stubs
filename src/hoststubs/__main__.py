from __future__ import annotations

import shlex
import logging
import argparse
from pathlib import Path

from hoststubs.host import load_host, dump_arguments
from hoststubs.infer import infer


def main() -> None:
    parser = argparse.ArgumentParser(prog='hoststubs')
    commands = parser.add_subparsers(dest='command', required=True)

    command = commands.add_parser('dump-arguments', help='print the dump.py arguments for a host')
    command.add_argument('host')
    command.add_argument('out')

    command = commands.add_parser('infer', help='run pyright on the host Python source')
    command.add_argument('dump', type=Path)
    command.add_argument('search', type=Path, nargs='+', help='directory that holds host packages')

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')

    if args.command == 'dump-arguments':
        print(shlex.join(dump_arguments(load_host(args.host), args.out)))
    elif args.command == 'infer':
        infer(args.dump, args.search)


if __name__ == '__main__':
    main()
