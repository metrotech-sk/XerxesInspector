#!/usr/bin/env python3

# This Python file uses the following encoding: utf-8

from xerxes_protocol import (
    Leaf,
    XerxesNetwork,
    XerxesRoot
)
from serial import Serial, SerialException
from typing import List
import sys
import logging

log = logging.getLogger(__name__)

class Discover:
    def __init__(self):
        pass

    @staticmethod
    def get_com_port() -> List[Serial]:
        """Discover the COM port of the Xerxes device."""
        available_ports = []
        for portnum in range(1,100):
            try:
                portname = f"COM{portnum}"
                port = Serial(portname, timeout=.01, baudrate=115200)
                port.close()
                available_ports.append(portname)
            except SerialException:
                pass
        return available_ports
