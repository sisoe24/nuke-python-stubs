from __future__ import annotations

import json
import shlex
import shutil
import logging
import argparse
from pathlib import Path

from hoststubs.emit import emit
from hoststubs.host import REPO, load_host, dump_arguments
from hoststubs.infer import infer
from hoststubs.report import report, load_context, resolve_dump
from hoststubs.targets import probe_targets


def main() -> None:
    parser = argparse.ArgumentParser(prog='hoststubs')
    commands = parser.add_subparsers(dest='command', required=True)

    command = commands.add_parser('dump-arguments', help='print the dump.py arguments for a host')
    command.add_argument('host')
    command.add_argument('out')

    command = commands.add_parser('infer', help='run pyright on the host Python source')
    command.add_argument('dump', type=Path)
    command.add_argument('search', type=Path, nargs='+', help='directory that holds host packages')

    command = commands.add_parser('report', help='print the share resolved per evidence source')
    command.add_argument('dump', type=Path)

    command = commands.add_parser('probe-targets', help='write the list of calls for probe.py')
    command.add_argument('dump', type=Path)
    command.add_argument('out', type=Path)
    command.add_argument('modules', nargs='+', help='only targets under these modules')

    command = commands.add_parser('build', help='write the stubs for one dumped version')
    command.add_argument('dump', type=Path)

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')

    if args.command == 'dump-arguments':
        print(shlex.join(dump_arguments(load_host(args.host), args.out)))
    elif args.command == 'infer':
        infer(args.dump, args.search)
    elif args.command == 'build':
        context = load_context(args.dump)
        out = REPO / 'build' / f'{context.dump.host}-{context.dump.host_version}'
        if out.exists():
            shutil.rmtree(out)
        written = emit(context, out)
        logging.info('Wrote %d files under %s.', len(written), out)
    elif args.command == 'report':
        print(report(args.dump))
    elif args.command == 'probe-targets':
        # Targets come from the docstrings alone, so a probe run cannot change its own input.
        dump, resolved = resolve_dump(args.dump, use_probe=False)
        targets = [
            target for target in probe_targets(dump, resolved, load_host(dump.host))
            if target['path'].startswith(tuple(f'{module}.' for module in args.modules))
        ]
        args.out.write_text(json.dumps({'targets': targets}, indent=1) + '\n', encoding='utf-8')
        logging.info('Wrote %s: %d targets.', args.out, len(targets))


if __name__ == '__main__':
    main()
