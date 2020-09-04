from simulator.simulatorBases.CrownstoneCore import CrownstoneCore
from simulator.simulatorBases.GuiCrownstoneCore import GuiCrownstoneCore


class SimulatorCrownstone(GuiCrownstoneCore):
    
    def __init__(self, id, x, y):
        super().__init__(id=id,x=x,y=y)
        self.myValue = False
       
    def resetState(self, resetTrainingData = True):
        self.myValue = False

    # overloaded
    def receiveMessage(self, data, rssi):
        print(self.id, "I HAVE A MESSAGE FROM", data["sender"], " SAYING ", data["payload"])

    # overloaded
    def newMeasurement(self, data, rssi):
        print(self.time, self.id, "Scans indicate", data["address"], " with payload ", data["payload"], " and rssi:", rssi)
        
        if rssi > -45:
            self.sendMessage("I saw a beacon with more that -45 dB!" + str(rssi) + "   " + str(self.time))

        self.sendMessage("I measured something" + str(rssi) + "   " + str(self.time))
            