#!/usr/bin/env python3

import json

from config import config
from utils.utils import utils

class config_parser:
    def __init__(self):
        self.config = config()

    def parse(self, config):
        u = utils()

        fd = open(config)
        json_data = json.load(fd)

        self.config.eth_config.enable = json_data["eth"]["enable"]

        src_mac = json_data["eth"]["src_mac"]
        self.config.eth_config.src_mac = u.get_mac_from_str(src_mac)

        dst_mac = json_data["eth"]["dst_mac"]
        self.config.eth_config.dst_mac = u.get_mac_from_str(dst_mac)

        self.config.eth_config.ethertype = int(json_data["eth"]["ethertype"], 16)
        self.config.eth_config.randomize = int(json_data["eth"]["randomize"])
        self.config.eth_config.inter_pkt_gap_us = int(json_data["eth"]["inter_pkt_gap_us"])
        self.config.eth_config.repeat = int(json_data["eth"]["repeat"])

    def get_config(self):
        return self.config

    def print(self):
        self.config.print()
