"""Tensorflow playground main dispatcher."""

import argh
import argparse

from tensor import __version__
from tensor.example import example


def main():
    """Main function."""
    p = argh.ArghParser(formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument(
        '--version', action='version', version="%(prog)s " + __version__)
    p.add_commands([example])
    p.dispatch()


if __name__ == '__main__':
    main()
