import pyxel
import random
import enum
import time
import collections

WIDTH = 192
HEIGHT = 128

SPEED = 5.9

RESOURCES = "Assets/resources.pyxres"
class Direction(enum.Enum):
    RIGHT = 0
    LEFT  = 1
    DOWN  = 2
    UP    = 3
    
class GameState(enum.Enum):
    RUNNING  = 0
    GAMEOVER = 1

class SceneGame:
    def __init__(self):
        self.tm = 0
        self.u = 0
        self.v = 0
        self.w = 24
        self.h = 16
        
    def draw(self):
        pyxel.bltm(0,0,self.tm,self.u,self.v,self.w,self.h,0)
class Coin():
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,0)
        
    def randomPosition(self):
        self.x = random.randrange(0,pyxel.width,self.w)
        self.y = random.randrange(0,pyxel.height,self.h)
        
    def IsColliding(self, other):
        return self.x < other.x + other.w and \
            self.x + self.w > other.x and \
            self.y < other.y + other.h and \
            self.y + self.h > other.y
        
class SnakeSection():
    def __init__(self,x,y,isHead=False):
        
        self.x = x
        self.y = y
        
        self.w = 8
        self.h = 8
        
        self.isHead = isHead
        
    def draw(self,direction):
        
        width = self.w
        height = self.h
        
        spriteX = 0
        spriteY = 0 
        
        if self.isHead:
            
            if direction == Direction.RIGHT:
                spriteX = 8
                spriteY = 0
            if direction == Direction.LEFT:
                spriteX = 8
                spriteY = 0
                width = width * -1
                
            if direction == Direction.UP:
                spriteX = 0
                spriteY = 8
                height = height * -1

            if direction == Direction.DOWN:
                spriteX = 0
                spriteY = 8
                
        pyxel.blt(self.x,self.y,0,spriteX,spriteY,width,height,0)
        
class App():
    
    def __init__(self,WIDHT,HEIGHT):
        
        pyxel.init( width      = WIDHT,
                    height     = HEIGHT,
                    caption    = "Snake",
                    fps        = 60,
                    fullscreen = True, 
                    scale      = 8 )
        
        pyxel.load(RESOURCES)
                
        self.coin = Coin(WIDHT/2,HEIGHT/2)
        
        self.snake = []
        
        self.queueSnakeInput = collections.deque()
        self.scene = SceneGame()
        
        pyxel.mouse(True)
        
        self.playMusic = True

        self.startNewGame()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        
        self.chackInput()

        if self.currentGameState == GameState.GAMEOVER:
            if (pyxel.btnp(pyxel.KEY_R)==True):
                self.startNewGame()
                
        if self.currentGameState == GameState.RUNNING:
            timeThisFrame = time.time()
            self.dt = timeThisFrame - self.timeLastFrame
            self.timeLastFrame = timeThisFrame
            self.timeSinceLastMove += self.dt
            
            if self.timeSinceLastMove >= 1/self.snakeSpeed:
                self.timeSinceLastMove = 0
                self.moveSnake()
            
            self.checkColisions()
            

    def draw(self):
        pyxel.cls(0)
        self.scene.draw()
        self.coin.draw()
        for s in self.snake:
            s.draw(self.snakeDirection)

            
    def moveSnake(self):
        
        if len(self.queueSnakeInput):
            self.snakeDirection = self.queueSnakeInput.popleft()
                
        previousLocationX = self.snake[0].x
        previousLocationY = self.snake[0].y
        
        if self.snakeDirection == Direction.RIGHT:
            self.snake[0].x += self.snake[0].w
        if self.snakeDirection == Direction.LEFT:
            self.snake[0].x -= self.snake[0].w
        if self.snakeDirection == Direction.UP:
            self.snake[0].y -= self.snake[0].h
        if self.snakeDirection == Direction.DOWN:
            self.snake[0].y += self.snake[0].h
            
        for s in self.snake:
            
            if s == self.snake[0]: continue
            
            currentLocationX = s.x
            currentLocationY = s.y
            
            s.x = previousLocationX
            s.y = previousLocationY
            
            previousLocationX = currentLocationX
            previousLocationY = currentLocationY
            
        
    def addSection(self):
        self.snake.append(SnakeSection(self.snake[-1].x, self.snake[-1].y))
        
    def chackInput(self):
        
        if (pyxel.btnp(pyxel.KEY_SPACE)==True):
            self.coin.randomPosition()
            self.addSection()
            print(pyxel.tilemap(0).get((self.snake[0].x/8), (self.snake[0].y/8)))
            print(pyxel.frame_count)
        
        if (pyxel.btnp(pyxel.KEY_M)==True):
            self.playMusic = not(self.playMusic)
            self.togleMusic()
        
        if len(self.queueSnakeInput) == 0:
            if (pyxel.btnp(pyxel.KEY_W)==True and self.snakeDirection != Direction.UP and self.snakeDirection != Direction.DOWN):
                self.queueSnakeInput.append(Direction.UP)

            elif (pyxel.btnp(pyxel.KEY_S)==True and self.snakeDirection != Direction.UP and self.snakeDirection != Direction.DOWN):
                self.queueSnakeInput.append(Direction.DOWN)
                
            elif (pyxel.btnp(pyxel.KEY_A)==True and self.snakeDirection != Direction.RIGHT and self.snakeDirection != Direction.LEFT):
                self.queueSnakeInput.append(Direction.LEFT)
                
            elif (pyxel.btnp(pyxel.KEY_D)==True and self.snakeDirection != Direction.RIGHT and self.snakeDirection != Direction.LEFT):
                self.queueSnakeInput.append(Direction.RIGHT)
                
        else:
            
            if (pyxel.btnp(pyxel.KEY_W)==True and self.queueSnakeInput[-1] != Direction.UP and self.queueSnakeInput[-1] != Direction.DOWN):
                self.queueSnakeInput.append(Direction.UP)

            elif (pyxel.btnp(pyxel.KEY_S)==True and self.queueSnakeInput[-1] != Direction.UP and self.queueSnakeInput[-1] != Direction.DOWN):
                self.queueSnakeInput.append(Direction.DOWN)
                
            elif (pyxel.btnp(pyxel.KEY_A)==True and self.queueSnakeInput[-1] != Direction.RIGHT and self.queueSnakeInput[-1] != Direction.LEFT):
                self.queueSnakeInput.append(Direction.LEFT)
                
            elif (pyxel.btnp(pyxel.KEY_D)==True and self.queueSnakeInput[-1] != Direction.RIGHT and self.queueSnakeInput[-1] != Direction.LEFT):
                self.queueSnakeInput.append(Direction.RIGHT)
            
    def isColliding(self, other):
        return self.snake[0].x < other.x + other.w and \
            self.snake[0].x + self.snake[0].w > other.x and \
            self.snake[0].y < other.y + other.h and \
            self.snake[0].y + self.snake[0].h > other.y
    
    def checkColisions(self):
        #TAIL
        for s in self.snake:
            if s == self.snake[0]: continue
            if self.isColliding(s) == True:
                self.currentGameState = GameState.GAMEOVER
                self.playSound("explosion")
                
        #COIN

        checkPositionCoin = False

        for s in self.snake:
            
            if s == self.snake[0]: 
                if self.coin.IsColliding(s):
                    self.addSection()
                    self.coin.randomPosition() 
                    checkPositionCoin = True
                    self.snakeSpeed += (self.snakeSpeed * 0.01)
                    self.playSound("coin")
                    
        if (self.coin.IsColliding(s) and checkPositionCoin) or (pyxel.tilemap(0).get((self.coin.x/8), (self.coin.y/8))==33):
            self.coin.randomPosition()
            
            
        #WALL
        
        if pyxel.tilemap(0).get((self.snake[0].x/8), (self.snake[0].y/8))==33:
            self.currentGameState = GameState.GAMEOVER
            self.playSound("explosion")
                
    def startNewGame(self):
        
        self.snake.clear()
        self.snakeSpeed = SPEED
        self.snake.append(SnakeSection(32,pyxel.height/2,isHead=True))
        self.snake.append(SnakeSection(24,pyxel.height/2))
        self.snake.append(SnakeSection(18,pyxel.height/2))
        self.snakeDirection: Direction = Direction.RIGHT
        
        self.coin.x = pyxel.width/2
        self.coin.y = pyxel.height/2
        
        self.timeLastFrame = time.time()
        self.timeSinceLastMove = 0
        self.dt = 0
        
        self.queueSnakeInput.clear()
        
        self.currentGameState = GameState.RUNNING
        
        if self.playMusic:
            pyxel.playm(0,loop=True)
            
    def togleMusic(self):
        if self.playMusic:
            pyxel.playm(0,loop=True)
        else: 
            pyxel.stop()
            
    def playSound(self,sound):
        if sound == "coin":
            pyxel.play(1,0)
        elif sound == "explosion":
            pyxel.stop()
            pyxel.play(2,1)
            
App(WIDTH,HEIGHT)
