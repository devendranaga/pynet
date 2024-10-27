#!/usr/bin/env python3

import sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from packet.packet import packet

class eth_hdr:
    def __init__(self):
        self.src_mac = []
        self.dst_mac = []
        self.ethertype = 0

    def serialize(self, pkt : packet):
        pkt.serialize_mac(self.dst_mac)
        pkt.serialize_mac(self.src_mac)
        pkt.serialize_2_bytes(self.ethertype)

