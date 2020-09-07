# we need to import this in order to be able to import the simulator
# it does not have to do anything other than be imported.
from examples.util import path

from examples.originalExample.exampleCrownstones.SimulatorCrownstone import SimulatorCrownstone
from examples.nearestCrownstoneAlgorithm.CrownstoneRunningNca import CrownstoneRunningNca
from examples.nearestCrownstoneAlgorithm.TrackableDeviceForNca import TrackableDeviceForNca
from examples.originalExample.exampleInteractionModules.TrainingAndTesting import TrainingAndTesting
from simulator import SimulationGui, JsonFileStore, Simulator

mapData = JsonFileStore('./maps/officesExample.json').getData()
config = JsonFileStore('./maps/config.json').getData()
rooms = JsonFileStore('./maps/roomOverlay.json').getData()
userModule = JsonFileStore('./maps/userData.json').getData()


simulatorCrownstones = [
    CrownstoneRunningNca("crownstone1", 0,   12), # X, Y positions in meters relative to zeroPoint on Map
    CrownstoneRunningNca("crownstone2", 0,  0), # X, Y positions in meters relative to zeroPoint on Map
    CrownstoneRunningNca("crownstone3", 10,   5), # X, Y positions in meters relative to zeroPoint on Map
]


simulationBroadcaster = TrackableDeviceForNca(userModule["address"], None)
simulationBroadcaster.setBroadcastParameters(intervalMs=userModule["intervalMs"], payload=userModule["payload"])
### mesh topology


### Broadcaster

# create a custom interaction module

a = SimulationGui()
a.loadMap(mapData)
a.loadSimulatorCrownstones(simulatorCrownstones)
a.loadUserData(userModule)
a.loadConfig(config)
a.loadRooms(rooms)


b = Simulator()
b.loadInteractionModule(TrainingAndTesting("Test"))
b.loadCrownstones(simulatorCrownstones)
b.loadConfig(config)
a.loadSimulator(b) # this will load the user module into the simulator as a broadcaster.

a.addBroadCaster(simulationBroadcaster) # can only be added after simulator is loaded atm, as broadcaster needs to be put into that.

a.run()
a.startSimulation(2)

