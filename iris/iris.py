
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging


__author__ = "Sanjeev Shrestha"
__copyright__ = "Sanjeev Shrestha"
__license__ = "gpl3"

_logger = logging.getLogger(__name__)



def run():
    """Entry point for console_scripts
    """
    print(sys.argv[1:])


if __name__ == "__main__":
    run()