class SimulationComponent:
    """
    Interface description:
    Objects deriving from this class represent components that can be attached to the SimulationCore.

    When attached the SimulationCore will call the respective tick() method.
    """
    def tick(self, simulationtimestamp):
        pass