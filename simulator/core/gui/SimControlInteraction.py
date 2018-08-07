from simulator.core.gui.SimControlPanels import ControlModes
from simulator.core.gui.SimOverlays import OverlayModes


class SimControlInteraction:
    gui = None
    
    def __init__(self, simulationGui):
        self.gui = simulationGui
        
    def toggleNValueOverlay(self):
        self._toggleOverlay(OverlayModes.NVALUE)
        
    def toggleRSSIOverlay(self):
        self._toggleOverlay(OverlayModes.RSSI)
        
    def toggleSTDOverlay(self):
        self._toggleOverlay(OverlayModes.STD)
        
    def toggleRSSICalibrationOverlay(self):
        self._toggleOverlay(OverlayModes.RSSI_CALIBRATION)
        
    def deselectCrownstone(self):
        self.gui.selectedCrownstone = None
        
    def _toggleOverlay(self, value):
        if self.gui.selectedOverlayMode == value:
            self.gui.selectedOverlayMode = OverlayModes.DISABLED
        else:
            self.gui.selectedOverlayMode = value
            
            
    def controlOverlayMode(self):
        self.gui.controlMode = ControlModes.OVERLAYS

    def controlUserMovementMode(self):
        self.gui.controlMode = ControlModes.USER_MOVEMENT

    def controlSelectMode(self):
        self.gui.controlMode = ControlModes.SELECT
        
    def controlSimulatorMode(self):
        self.gui.controlMode = ControlModes.SIMULATOR
        
        
    def togglePathDrawing(self):
        self.gui.state["pathDrawing"] = not self.gui.state["pathDrawing"]
        
    def toggleDrawRoomOverlays(self):
        self.gui.drawRoomOverlays = not self.gui.drawRoomOverlays
    
    def toggleDrawSourceCrownstones(self):
        self.gui.drawSourceCrownstones = not self.gui.drawSourceCrownstones
    
    def toggleDrawSourceBeacons(self):
        self.gui.drawSourceBeacons = not self.gui.drawSourceBeacons
    
    def toggleDrawUserPath(self):
        self.gui.drawUserPath = not self.gui.drawUserPath
        
    def toggleDrawUserPathIndicator(self):
        self.gui.drawUser = not self.gui.drawUser
        
    def toggleDrawUserPathTimes(self):
        self.gui.drawUserPathTimes = not self.gui.drawUserPathTimes
        
    def toggleDrawSimulationCrownstones(self):
        self.gui.drawSimulationCrownstones = not self.gui.drawSimulationCrownstones
        
        
    def startSimulation(self):
        self.gui.startSimulation()
        
    def simulate5Seconds(self):
        self.gui.simulator.continueSimulation(5)
        
    def runSimulation(self):
        self.gui.runSimulation()
        
    def stopSimulation(self):
        self.gui.simulationRunning = False
        
        