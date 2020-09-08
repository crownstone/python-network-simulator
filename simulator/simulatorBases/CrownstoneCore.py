from simulator.topics.Topics import Topics
from simulator.simulatorBases.SimulationComponent import SimulationComponent

class CrownstoneCore(SimulationComponent):
    def __init__(self, id):
        self.id = id
        self.eventBus = None
        self.time = 0
        self.debugPrint = False
        self.debugInformation = {}

    def print(self, *data):
        if self.debugPrint:
            print(data)
        
    def setTime(self, time):
        self.time = time

    def loadEventBus(self, eventBus):
        self.eventBus = eventBus
    
    def sendMessage(self, data, ttl = 5, repeat = 3):
        self.eventBus.emit(Topics.meshMessage, {"sender": self.id, "payload": data, "ttl": ttl, "repeat": repeat})
    
    def receiveMessage(self, data, rssi):
        """
            This is where mesh messages are received
            :param data:  { "sender":string, "payload": dictionary }
        """
        pass
    
    def newMeasurement(self, data, rssi):
        """
            This is where scanned ble devices are seen
            :param data:  { "address":string, "payload": dictionary }
        """
        pass
    
    def tick(self, time):
        pass
    
    def publishResult(self, roomId):
        self.eventBus.emit(Topics.gotResult, {"sender": self.id, "roomId": roomId})
        
    def resetState(self, resetTrainingData = True):
        """
            This is an important method to reset any state the Crownstone may have so the simulation can be restarted.
            If resetTrainingData is False, you should clear all state data except that referring to the training sets.
        """
        pass