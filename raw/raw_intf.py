#!/usr/bin/env python3

import socket

class raw_types:
    ETH_P_ALL = 3

class raw_intf:
    def __init__(self, intf):
        self.raw_fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0)
        self.raw_fd.bind((intf, raw_types.ETH_P_ALL))

    def send(self, msg):
        self.raw_fd.send(msg)

    def recv(self):
        msg = self.raw_fd.recv(1500)
        return msg
