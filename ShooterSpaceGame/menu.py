import pyxel
import buttons
import server
from keyboardInput import KeyboardInput

class Menu():
    def __init__(self):
        self.state = 0
        self.internalState = 0
        self.online = False
        self.buttons = [
            buttons.Button([pyxel.width/2,80 ],[100,10],[12,5,1],['ENTRENAMIENTO LOCAL',6] ), # LOCAL
            buttons.Button([pyxel.width/2-pyxel.width/4,100 ],[70,10],[12,5,1],['CREAR SERVIDOR',6] ), # CLIENT
            buttons.Button([pyxel.width/2+pyxel.width/4,100],[80,10],[12,5,1],['UNIRSE A SERVIDOR',6] ), # SERVER
        ]
        self.returnButton = buttons.Button([25,10 ],[50,10],[7,0,0],['VOLVER',13])
        
        self.connectButton = buttons.Button([pyxel.width/2,100],[80,10],[12,5,1],['UNIRSE A SERVIDOR',6] )
        
        self.addrInput = KeyboardInput('192.168.')
        self.addrBox = buttons.Button([pyxel.width/2,45],[100,10],[7,0,0],[self.addrInput.storage,3] )
        self.portInput = KeyboardInput('8000')
        self.portBox = buttons.Button([pyxel.width/2,85],[100,10],[7,0,0],[self.portInput.storage,3] )
        
    def update(self):
        
        for button in self.buttons:
            button.update()
            
        if (self.returnButton.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): 
            if (self.online):
                self.multiplayer.closeConection()
            else:
                self.internalState = 0
        
        if (self.internalState == 0):
            self.addrBox.active = False
            self.portBox.active = False
            for button in self.buttons:
                button.active = True
            for i in range(len(self.buttons)):
                if (self.buttons[i].isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.actionButtonMenu(i)
                
        
        if (self.internalState == 1):
            for button in self.buttons:
                button.active = False
            self.addrBox.active = False
            self.portBox.active = False
            self.returnButton.active = True
            
            
        if (self.internalState == 2):
            self.returnButton.active = True
            self.addrBox.active = True
            self.portBox.active = True
            for button in self.buttons:
                button.active = False
                
            if (self.addrBox.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.addrInput.active = True
            elif (self.addrBox.isColliding() == False and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.addrInput.active = False
            
            if (self.portBox.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.portInput.active = True
            elif (self.portBox.isColliding() == False and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.portInput.active = False

            if (self.addrInput.active == True):
                self.addrInput.update()
                self.addrBox.text[1] = 11
                self.addrBox.text[0] = self.addrInput.storage
            else: self.addrBox.text[1] = 3
                        
            if (self.portInput.active == True):
                self.portInput.update()
                self.portBox.text[1] = 11
                self.portBox.text[0] = self.portInput.storage
            else: self.portBox.text[1] = 3
        
    def draw(self):
        
        if (self.internalState == 0):
            pyxel.cls(6)
            pyxel.text(((pyxel.width/2)-((len('ASTEROID ONLINE LAN')*pyxel.FONT_WIDTH)/2)),25,'ASTEROID ONLINE LAN',5)
            pyxel.text(((pyxel.width/2)-((len('POR JOSEPH RIOS H')*pyxel.FONT_WIDTH)/2)),32,'POR JOSEPH RIOS H',12)
            for button in self.buttons:
                button.draw()
        else:
            if (self.internalState == 1):
                pyxel.cls(10)
                pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("Direccion IP LAN")),50,"Direccion IP LAN", 9)
                pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("Puerto actual")),70,"Puerto actual", 9)
                try:
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len(self.multiplayer.ip)),60,self.multiplayer.ip, 9)
                except:
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("ERROR")),60,"ERROR", 9)
                    
                try:
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len(self.multiplayer.port)),80,self.multiplayer.port, 9)
                except: 
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("ERROR")),80,"ERROR", 9)
                    
                
            if (self.internalState == 2):
                pyxel.cls(11)
                pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("Direccion IP LAN")),30,"Direccion IP LAN", 3)
                pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("Puerto")),70,"Puerto", 3)
                self.addrBox.draw()
                self.portBox.draw()
                
            self.returnButton.draw()
            
    def actionButtonMenu(self,index):
        if (index == 0): self.state = 1
        if (index == 1): 
            self.internalState = 1
            self.multiplayer = server.Conection()
        if (index == 2): self.internalState = 2
            