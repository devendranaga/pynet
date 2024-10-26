#!/usr/bin/env python3

import os
import sys

import logging

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from base.cmdargs import cmdargs
from raw.raw_intf import raw_intf

class pynet:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.cmd_args = cmdargs()
        self.cmd_args.parse()

        self.raw_intf = raw_intf(self.cmd_args.interface)

pynet = pynet()
