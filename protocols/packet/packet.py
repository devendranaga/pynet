#!/usr/bin/env python3

class packet:
    def __init__(self):
        self.pkt_buf = []
        self.off = 0

    def serialize_mac(self, mac):
        for i in mac:
            self.pkt_buf.append(i)

    def serialize_2_bytes(self, val):
        self.pkt_buf.append((val & 0xFF00) >> 8)
        self.pkt_buf.append(val & 0x00FF)
