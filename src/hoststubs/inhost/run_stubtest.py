"""Run mypy's stubtest inside the host, so it can import the real modules.

Usage:
    <host python> run_stubtest.py MYPY_DIR STUBTEST_ARGUMENT...

MYPY_DIR holds a mypy installed for the host's Python version, without
compiled modules: the compiled build does not load inside Nuke.
scripts/stubtest.sh prepares it and calls this script.
"""
import sys


def main(argv):
    sys.path.insert(0, argv[0])
    from mypy import stubtest

    try:
        code = stubtest.test_stubs(stubtest.parse_options(argv[1:]))
    except SystemExit as error:
        code = error.code
    sys.stdout.write('stubtest exit code: {}\n'.format(code))


if __name__ == '__main__':
    main(sys.argv[1:])
