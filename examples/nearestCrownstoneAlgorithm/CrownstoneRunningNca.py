from simulator.simulatorBases.GuiCrownstoneCore import GuiCrownstoneCore
from examples.nearestCrownstoneAlgorithm.PingMessages import PingMessage

class CrownstoneRunningNca(GuiCrownstoneCore):
    """
    Crownstone mesh node that simulates the nearest crownstone algorithm.
    """
    def __init__(self, id, x, y):
        super().__init__(id=id, x=x, y=y)
        self.resetState()

    # (also called at init)
    def resetState(self, resetTrainingData=True):
        self.pingmessages = []

    # overloaded
    def receiveMessage(self, data, rssi):
        self.pingmessages.append(PingMessage(self.time, data["sender"], self.id, rssi))
        print("receive message: ", self.pingmessages[-1])
        # TODO: check data for winning messages, record time, and possibly resend message to push result.

    # overloaded
    def newMeasurement(self, data, rssi):
        self.pingmessages.append(PingMessage(self.time, data["address"], self.id, rssi))
        print("new measurement: ", self.pingmessages[-1])
        # print(self.time, self.id, "Scans indicate", data["address"], " with payload ", data["payload"], " and rssi:",
        #       rssi)

    # overloaded
    def tick(self, time):
        # TODO: if time out happens (depends on mesh diameter or local eccentricity) we can be sure about the result.
        # TODO: in that case, update our belief.
        pass