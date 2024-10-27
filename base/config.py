#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)

class eth_config:
    def __init__(self):
        self.enable             = False
        self.src_mac            = []
        self.dst_mac            = []
        self.ethertype          = 0
        self.randomize          = False
        self.inter_pkt_gap_us   = 0
        self.repeat             = False

    def is_enabled(self):
        return self.enable

    def print(self):
        logger.info("eth: {")
        logger.info("\t enable: " +  str(self.enable))
        logger.info("\t src_mac: " + str(self.src_mac))
        logger.info("\t dst_mac: " + str(self.dst_mac))
        logger.info("\t ethertype: " + str(hex(self.ethertype)))
        logger.info("\t randomize: " + str(self.randomize))
        logger.info("\t inter_pkt_gap_ns: " + str(self.inter_pkt_gap_us))
        logger.info("\t repeat: " + str(self.repeat))
        logger.info("}")

class config:
    def __init__(self):
        self.eth_config = eth_config()

    def get_eth_config(self):
        return self.eth_config

    def print(self):
        self.eth_config.print()
