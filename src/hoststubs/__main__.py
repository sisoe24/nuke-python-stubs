from __future__ import annotations

import json
import shlex
import shutil
import logging
import argparse
from pathlib import Path

from hoststubs import ir
from hoststubs.build import build
from hoststubs.host import REPO, load_host, dump_arguments
from hoststubs.infer import infer
from hoststubs.report import report, resolve_dump
from hoststubs.targets import param_targets, probe_targets


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

    for name, script in (('probe-targets', 'probe.py'), ('param-targets', 'param_probe.py')):
        command = commands.add_parser(name, help=f'write the list of calls for {script}')
        command.add_argument('dump', type=Path)
        command.add_argument('out', type=Path)
        command.add_argument('modules', nargs='+', help='only targets under these modules')

    command = commands.add_parser('build', help='write and check the stubs for one dumped version')
    command.add_argument('dump', type=Path)
    command.add_argument(
        '--update-snapshot', action='store_true',
        help='record what pyright reveals for the corpus instead of checking it',
    )

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')

    if args.command == 'dump-arguments':
        print(shlex.join(dump_arguments(load_host(args.host), args.out)))
    elif args.command == 'infer':
        infer(args.dump, args.search)
    elif args.command == 'build':
        dump = ir.load(args.dump)
        out = REPO / 'build' / f'{dump.host}-{dump.host_version}'
        findings = build(args.dump, out, args.update_snapshot)

        for finding in findings:
            logging.error(finding)
        if findings:
            raise SystemExit(f'Gate failed: {len(findings)} findings.')
        logging.info('Gate passed.')

        # The committed tree that editors read, one folder per host version.
        shipped = REPO / 'stubs' / dump.host_version
        shutil.rmtree(shipped, ignore_errors=True)
        shutil.copytree(out / 'stubs', shipped)
        logging.info('Replaced %s with the built stubs.', shipped)
    elif args.command == 'report':
        print(report(args.dump))
    elif args.command in ('probe-targets', 'param-targets'):
        # Targets come from the docstrings alone, so a probe run cannot change its own input.
        dump, resolved = resolve_dump(args.dump, use_overrides=False, use_probe=False)
        choose = probe_targets if args.command == 'probe-targets' else param_targets
        targets = [
            target for target in choose(dump, resolved, load_host(dump.host))
            if target['path'].startswith(tuple(f'{module}.' for module in args.modules))
        ]
        args.out.write_text(json.dumps({'targets': targets}, indent=1) + '\n', encoding='utf-8')
        logging.info('Wrote %s: %d targets.', args.out, len(targets))


if __name__ == '__main__':
    main()
