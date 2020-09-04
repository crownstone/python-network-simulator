from simulator.simulatorBases.CrownstoneCore import CrownstoneCore
from simulator.simulatorBases.GuiCrownstoneCore import GuiCrownstoneCore


class CrownstoneRunningNca(GuiCrownstoneCore):
    """
    Crownstone mesh node that simulates the nearest crownstone algorithm.
    """
    def __init__(self, id, x, y):
        super().__init__(id=id, x=x, y=y)
        self.myValue = False

    def resetState(self, resetTrainingData=True):
        self.myValue = False

    # overloaded
    def receiveMessage(self, data, rssi):
        print(self.id, "I HAVE A MESSAGE FROM", data["sender"], " SAYING ", data["payload"])
        # TODO: check data for winning messages, record time, and possibly resend message to push result.

    # overloaded
    def newMeasurement(self, data, rssi):
        print(self.time, self.id, "Scans indicate", data["address"], " with payload ", data["payload"], " and rssi:",
              rssi)

    # overloaded
    def tick(self, time):
        # TODO: if time out happens (depends on mesh diameter or local eccentricity) we can be sure about the result.
        # TODO: in that case, update our belief.
        pass