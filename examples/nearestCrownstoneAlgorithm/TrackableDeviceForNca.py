from simulator.simulatorBases.BroadcasterCore import BroadcasterCore

class TrackableDeviceForNca(BroadcasterCore):

    def __init__(self, address):
        super().__init__(address="address")
        self.pathIndex = 0
        self.pathTime = 0
        self.time = 0

        self.pathFinished = False
        self.pos = [self.gui.simUserMovement.path[0][0], self.gui.simUserMovement.path[0][1]]

    def getRssiToCrownstone(self, targetCrownstoneId):
        # get xyz coords of crownstoneId
        targetCrownstone = self.gui.simulatorCrownstonesMap[targetCrownstoneId]
        # calculate position of user
        rssi = self.gui.simMath.getRssiUserToCrownstone(targetCrownstone.pos, self.pos)
        return rssi

    def tick(self, simulationTime):
        """
        Updates the position of the device in x,y plane based on the path that is set and the walking speed.
        """
        self.time = simulationTime
        lastPathPoint = None
        userSpeed = self.gui.config["userWalkingSpeed"]

        if self.pathFinished:
            return

        for i in range(self.pathIndex, len(self.gui.simUserMovement.path)):
            pathPoint = self.gui.simUserMovement.path[i]
            if lastPathPoint is not None:
                dx = pathPoint[0] - lastPathPoint[0]
                dy = pathPoint[1] - lastPathPoint[1]
                distance = math.sqrt(dx ** 2 + dy ** 2)
                dt = distance / userSpeed

                self.pathTime += dt
                if self.pathTime > simulationTime:
                    ddt = (simulationTime - (self.pathTime - dt)) / dt
                    self.pos[0] = lastPathPoint[0] + dx * ddt
                    self.pos[1] = lastPathPoint[1] + dy * ddt
                    self.pathIndex = i - 1
                    self.pathTime -= dt
                    break
                elif i == len(self.gui.simUserMovement.path) - 1:
                    self.pathFinished = True
            lastPathPoint = pathPoint
