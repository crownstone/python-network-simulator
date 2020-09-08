from simulator.simulatorBases.SimulationComponent import SimulationComponent

class SimulationInspector(SimulationComponent):
    """
    Component to attach to SimulatorCore in order to inspect it.
    """
    def __init__(self, period_s: float, simulator):
        self.simulator = simulator
        self.period_s = period_s
        self.last_inspect_call_time = float("-inf")

    def tick(self, simulationTime):
        if simulationTime > self.last_inspect_call_time + self.period_s:
            self.inspect(self.simulator)


    def inspect(self, simulator):
        pass