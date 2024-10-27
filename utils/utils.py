#!/usr/bin/env python3

class utils:
    def get_mac_from_str(self, mac_str):
        mac = []
        mac_list = mac_str.split(':')
        for i in mac_list:
            mac.append(int(i, 16))

        return mac
