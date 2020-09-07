from simulator.simulatorBases.CrownstoneCore import CrownstoneCore
from simulator.simulatorBases.BroadcasterCore import BroadcasterCore

class PingMessage:
    def __init__(self, timestamp, send, recv: CrownstoneCore, rssi):
        """
        """
        self.timestamp = timestamp
        self.sender = send
        self.recipient = recv
        self.rssi = rssi

    def __str__(self):
        return ",".join([str(k) + ": " + str(v) for k,v in self.__dict__.items()])

    def __repr__(self):
        return str(self)