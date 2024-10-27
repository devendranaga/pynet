#!/usr/bin/env python3


import os
import sys
import time
import logging

logger = logging.getLogger(__name__)

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from config import eth_config
from protocols.packet import packet

from protocols.l2.eth import eth_hdr
from raw import raw_intf

##
# perform ethernet packet replay
class ethernet_packet_replay:
    ##
    # initialize ethernet packet replay
    #
    # @param [in] self
    # @param [in] eth_cfg - ethernet configuration
    def __init__(self, eth_cfg : eth_config):
        self.eth_config = eth_cfg

    def repeat_msg(self, raw_fd : raw_intf, eh : eth_hdr):
         while self.eth_config.repeat:
            pkt = packet.packet()
            eh.serialize(pkt)
            sec = self.eth_config.inter_pkt_gap_us / 1000000
            time.sleep(sec)
            #logger.info("print ..")
            raw_fd.send(bytes(pkt.pkt_buf))

    def run(self, raw_fd : raw_intf):
            eh = eth_hdr()
            eh.dst_mac = self.eth_config.dst_mac
            eh.src_mac = self.eth_config.src_mac
            eh.ethertype = self.eth_config.ethertype

            pkt = packet.packet()
            eh.serialize(pkt)

            raw_fd.send(bytes(pkt.pkt_buf))
            self.repeat_msg(raw_fd, eh)

