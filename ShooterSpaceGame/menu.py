import pyxel
import buttons
import server
import client
from keyboardInput import KeyboardInput
import player

class Menu():
    def __init__(self):
        self.state = 0
        self.internalState = 0
        self.online = False
        self.initOnline = False
        self.buttons = [
            buttons.Button([pyxel.width/2,80 ],[100,10],[12,5,1],['ENTRENAMIENTO LOCAL',6] ), # LOCAL
            buttons.Button([pyxel.width/2-pyxel.width/4,100 ],[70,10],[12,5,1],['CREAR SERVIDOR',6] ), # CLIENT
            buttons.Button([pyxel.width/2+pyxel.width/4,100],[80,10],[12,5,1],['UNIRSE A SERVIDOR',6] ), # SERVER
        ]
        self.returnButton = buttons.Button([25,10 ],[50,10],[7,0,0],['VOLVER',13])
        
        self.connectButton = buttons.Button([pyxel.width/2,110],[80,10],[3,1,1],['UNIRSE A SERVIDOR',11] )
        self.hostButton = buttons.Button([pyxel.width/2,110],[80,10],[9,1,1],['CREAR SERVIDOR',10] )
        
        self.addrInput = KeyboardInput('192.168.')
        self.addrBox = buttons.Button([pyxel.width/2,65],[100,10],[7,0,0],[self.addrInput.storage,3] )
        self.portInput = KeyboardInput('8000')
        self.portBox = buttons.Button([pyxel.width/2,95],[100,10],[7,0,0],[self.portInput.storage,3] )
        self.nameInput = KeyboardInput('player')
        self.nameBox = buttons.Button([pyxel.width/2,35],[100,10],[7,0,0],[self.nameInput.storage,3] )
        self.player = player.Player(5,3,(pyxel.width/2),(pyxel.height/2),1)
        self.otherPlayer = player.Player(5,3,(pyxel.width/2),(pyxel.height/2),1,True)
        
    def update(self,reload):
        
        try:
            self.online = self.multiplayer.online
        except:
            self.online = False
        
        for button in self.buttons:
            button.update()
            
        if (self.returnButton.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): 
            if (self.online):
                self.multiplayer.closeConection()
                self.internalState = 0
            else:
                self.internalState = 0

                
        if (self.online):
            if (self.initOnline == False):
                self.initOnlineMethod()
                self.initOnline == True
                        
            self.player.update(reload)
            self.otherPlayer.update()
            
            self.multiplayer.my["pos"][0] = self.player.pos[0]
            self.multiplayer.my["pos"][1] = self.player.pos[1]
            self.multiplayer.my["angle"]  = self.player.angle
            self.multiplayer.my["shoot"]  = self.player.typeShoot
            self.player.typeShoot = 0
            
            self.otherPlayer.pos[0] = self.multiplayer.other["pos"][0]
            self.otherPlayer.pos[1] = self.multiplayer.other["pos"][1]
            self.otherPlayer.angle  = self.multiplayer.other["angle"]
            if (self.multiplayer.other["shoot"] != 0): self.otherPlayer.shoot(self.multiplayer.other["shoot"])
            
            for shoot in self.otherPlayer.shoots:
                shoot.isCollision(self.player.collisionObject.pos,self.player.collisionObject.r)
            for shoot in self.player.shoots:
                shoot.isCollision(self.otherPlayer.collisionObject.pos,self.otherPlayer.collisionObject.r)
            # self.multiplayer.other["shoot"] = 0
            
        else:
            
            if (self.internalState == 0):
                self.addrBox.active = False
                self.portBox.active = False
                self.hostButton.active = False
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
                                
                if (self.hostButton.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.hostConect()
                    
                if (self.nameBox.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.nameInput.active = True
                elif (self.nameBox.isColliding() == False and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.nameInput.active = False
                                
                if (self.nameInput.active == True):
                    self.nameInput.update()
                    self.nameBox.text[1] = 9
                    self.nameBox.text[0] = self.nameInput.storage
                else: self.nameBox.text[1] = 10
                
            if (self.internalState == 2):
                self.returnButton.active = True
                self.addrBox.active = True
                self.portBox.active = True
                for button in self.buttons:
                    button.active = False
                
                if (self.connectButton.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.clientConect()
                
                if (self.nameBox.isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.nameInput.active = True
                elif (self.nameBox.isColliding() == False and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.nameInput.active = False
                    
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
                
                if (self.nameInput.active == True):
                    self.nameInput.update()
                    self.nameBox.text[1] = 11
                    self.nameBox.text[0] = self.nameInput.storage
                else: self.nameBox.text[1] = 3
        
    def draw(self):
        if (self.online):
            self.player.draw()
            self.otherPlayer.draw()
        
        else:
            if (self.internalState == 0):
                pyxel.cls(6)
                pyxel.text(((pyxel.width/2)-((len('ASTEROID ONLINE LAN')*pyxel.FONT_WIDTH)/2)),25,'ASTEROID ONLINE LAN',5)
                pyxel.text(((pyxel.width/2)-((len('POR JOSEPH RIOS H')*pyxel.FONT_WIDTH)/2)),32,'POR JOSEPH RIOS H',12)
                for button in self.buttons:
                    button.draw()
            else:
                if (self.internalState == 1):
                    pyxel.cls(10)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("NICKNAME")),20,"NICKNAME", 9)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("DIRECCION IP")),50,"DIRECCION IP", 9)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("PUERTO")),80,"PUERTO", 9)
                    self.nameBox.draw()
                    self.hostButton.draw()
                    try:
                        pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len(self.multiplayer.ip)),60,self.multiplayer.ip, 9)
                    except:
                        pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("crea el servidor primero")),60,"crea el servidor primero", 9)
                        
                    try:
                        pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len(self.multiplayer.port)),90,self.multiplayer.port, 9)
                    except: 
                        pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("crea el servidor primero")),90,"crea el servidor primero", 9)
                        
                    
                if (self.internalState == 2):
                    pyxel.cls(11)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("NICKNAME")),20,"NICKNAME", 3)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("DIRECCION IP")),50,"DIRECCION IP", 3)
                    pyxel.text((pyxel.width/2)-((pyxel.FONT_WIDTH/2)*len("PUERTO")),80,"PUERTO", 3)
                    self.nameBox.draw()
                    self.addrBox.draw()
                    self.portBox.draw()
                    self.connectButton.draw()
                    
                self.returnButton.draw()
            
    def actionButtonMenu(self,index):
        if (index == 0): self.state = 1
        if (index == 1): 
            self.internalState = 1
            self.hostButton.active = True
        if (index == 2): self.internalState = 2
            
    def clientConect(self):
        self.multiplayer = client.Conection(self.addrInput.storage,int(self.portInput.storage))
        
    def hostConect(self):
        self.multiplayer = server.Conection()
        self.hostButton.active = False
        
    def initOnlineMethod(self):
        self.otherPlayer.name = self.multiplayer.other["name"]
        self.multiplayer.my["name"] = self.nameInput.storage
        self.player.name = self.nameInput.storage

