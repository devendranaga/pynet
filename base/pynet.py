#!/usr/bin/env python3

import os
import sys

import logging

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from base.cmdargs import cmdargs
from gen.eth import ethernet_packet_replay
from raw.raw_intf import raw_intf
from config_parser import config_parser

class pynet:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        logging.info("parse command line arguments")

        self.cmd_args = cmdargs()
        self.cmd_args.parse()

        logging.info("parse configuration")

        self.config_parser = config_parser()
        self.config_parser.parse(self.cmd_args.config)
        self.config_parser.print()

        logging.info("create raw socket on " + self.cmd_args.interface)

        self.raw_intf = raw_intf(self.cmd_args.interface)

        self.metadata = [
            {
                "config": self.config_parser.get_config().get_eth_config,
                "enabled": self.config_parser.get_config().get_eth_config().is_enabled,
                "replay_handle": ethernet_packet_replay
            }
        ]


    def replay(self):
        for i in self.metadata:
            config_data = i["config"]()
            if config_data.enable:
                handle = i["replay_handle"](i["config"]())
                handle.run(self.raw_intf)

pyn = pynet()
pyn.replay()
