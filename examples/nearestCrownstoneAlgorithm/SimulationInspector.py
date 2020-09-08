from simulator.simulatorBases.SimulationComponent import SimulationComponent
import numpy as np

class SimulationInspector(SimulationComponent):
    """
    Component to attach to SimulatorCore in order to inspect it.

    For now only explicit implementation for NCA.
    """
    def __init__(self, period_s: float, simulator):
        self.simulator = simulator
        self.period_s = period_s
        self.last_inspect_call_time = float("-inf")

    def tick(self, simulationTime):
        if simulationTime > self.last_inspect_call_time + self.period_s:
            self.last_inspect_call_time = simulationTime
            self.inspect(self.simulator)


    def inspect(self, simulator):
        closest_map = dict()
        for broadcaster in simulator.broadcasters:
            closest_stone = min(simulator.crownstones,
                                key=lambda crownstone: np.linalg.norm(np.array(broadcaster.pos) - np.array(crownstone.pos)))
            closest_map[broadcaster.address] = closest_stone.id

        print("inspect closest map: ", closest_map)
