import sys

import getopt

import logging

logger = logging.getLogger(__name__)

class cmdargs:
    def __init__(self):
        self.config = ""
        self.interface = ""

    def usage(self):
        logger.info("pynet [hf:i:]")
        logger.info("\t -h --help - print this help")
        logger.info("\t -f <filename> --filename - load json configuration")
        logger.info("\t -i <interface> --ifname - interface name")

    def parse(self):
        if len(sys.argv) == 1:
            self.usage()
            sys.exit(2)
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hf:i:", ["help", "filename=", "ifname="])
        except getopt.GetoptError as err:
            self.usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.usage()
                sys.exit(2)
            elif opt in ("-f", "--filename"):
                self.config = arg
            elif opt in ("-i", "--ifname"):
                self.interface = arg
            else:
                sys.exit(2)
