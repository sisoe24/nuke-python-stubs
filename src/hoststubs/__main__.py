from __future__ import annotations

import shlex
import argparse

from hoststubs.host import load_host, dump_arguments


def main() -> None:
    parser = argparse.ArgumentParser(prog='hoststubs')
    commands = parser.add_subparsers(dest='command', required=True)

    command = commands.add_parser('dump-arguments', help='print the dump.py arguments for a host')
    command.add_argument('host')
    command.add_argument('out')

    args = parser.parse_args()
    host = load_host(args.host)
    print(shlex.join(dump_arguments(host, args.out)))


if __name__ == '__main__':
    main()
