from __future__ import annotations

import shlex
import argparse

from hoststubs.host import load_host, dump_command


def main() -> None:
    parser = argparse.ArgumentParser(prog='hoststubs')
    commands = parser.add_subparsers(dest='command', required=True)

    command = commands.add_parser('dump-command', help='print the command that dumps a host')
    command.add_argument('host')
    command.add_argument('launcher')
    command.add_argument('out')

    args = parser.parse_args()
    host = load_host(args.host)
    print(shlex.join(dump_command(host, args.launcher, args.out)))


if __name__ == '__main__':
    main()
