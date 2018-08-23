from simulator.simulatorBases.InteractionCore import InteractionCore


class TrainingAndTesting(InteractionCore):
    
    targetParameters = None
    lastTime = 0
    
    ###
    # The name is the "address" of the user that broadcasts the messages
    ###
    def __init__(self, name):
        super().__init__(name)
        
    # override
    def tick(self, time):
        if time == 0:
            self.sendMessage("startTraining")
        
        if self.lastTime < 5 <= time:
            self.sendMessage("stopTraining")
        
        self.lastTime = time