import pygame,math

from enum import Enum

class OverlayModes(Enum):
    DISABLED = "DISABLED"
    RSSI = "RSSI"
    
class SimOverlays:
    
    gui = None
    blockSize = 10
    
    height = 1 #m
    
    def __init__(self, gui):
        self.gui = gui
        
    def draw(self, surface, mWidth, mHeight):
        if self.gui.selectedOverlayMode is None or self.gui.selectedOverlayMode == OverlayModes.DISABLED:
            return False

        if self.gui.selectedCrownstone is None:
            return False
        
        if self.gui.selectedOverlayMode == OverlayModes.RSSI:
            return self.drawRssiOverlay(surface, mWidth, mHeight)
        
            
            

    def drawRssiOverlay(self, surface, mWidth, mHeight):
        xBlockCount = math.ceil(mWidth/self.blockSize)
        yBlockCount = math.ceil(mHeight/self.blockSize)
        
        maxRSSI = -50
        minRSSI = -98
        
        self.gui.simColorRange.startRange = minRSSI
        self.gui.simColorRange.endRange   = maxRSSI
        
        targetCrownstone = None
        for crownstone in self.gui.simulatorCrownstones:
            if crownstone.id == self.gui.selectedCrownstone:
                targetCrownstone = crownstone
                break
                
        if targetCrownstone is None:
            return
        
        for i in range(0,xBlockCount):
            for j in range(0,yBlockCount):
                x,y   = self.gui.xyPxToZeroRefMeters(0.5*self.blockSize + i*self.blockSize, 0.5*self.blockSize + j*self.blockSize)
                
                rssi  = self.gui.simMath.getRssiToCrownstone(targetCrownstone, (x,y))
                
                if rssi is not None:
                    color = self.gui.simColorRange.getColor(rssi)
                    
                    pygame.draw.rect(surface, color, (i*self.blockSize, j*self.blockSize, self.blockSize, self.blockSize))

        return True
                


