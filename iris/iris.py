#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     iris = iris.iris:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
from iris.controller.iris import IrisBaseController

__author__ = "Sanjeev Shrestha"
__copyright__ = "Sanjeev Shrestha"
__license__ = "gpl3"

_logger = logging.getLogger(__name__)


def run():
    """Entry point for console_scripts
    """
    controller = IrisBaseController()
    controller.parse(sys.argv[1:])
    spoken = controller.listen()
    print(spoken)
    controller.respond(spoken)


if __name__ == "__main__":
    run()
