import pyxel
import random
import enum
import time

WIDTH = 192
HEIGHT = 128

SPEED = 5.9

RESOURCES = "Assets/resources.pyxres"
class Direction(enum.Enum):
    RIGHT = 0
    LEFT  = 1
    DOWN  = 2
    UP    = 3
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
        
        self.snake.append(SnakeSection(16,0,isHead=True))
        self.snake.append(SnakeSection(8,0))
        self.snake.append(SnakeSection(0,0))
        self.snakeDirection: Direction = Direction.RIGHT
        self.snakeSpeed = SPEED
        
        self.timeLastFrame = time.time()
        self.timeSinceLastMove = 0
        self.dt = 0
        
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        timeThisFrame = time.time()
        self.dt = timeThisFrame - self.timeLastFrame
        self.timeLastFrame = timeThisFrame
        self.timeSinceLastMove += self.dt
        if self.timeSinceLastMove >= 1/self.snakeSpeed:
            self.timeSinceLastMove = 0
            self.moveSnake()
                
        if (pyxel.btnp(pyxel.KEY_SPACE)==True):
            self.coin.randomPosition()
            self.addSection()
        if (pyxel.btn(pyxel.KEY_W)==True and self.snakeDirection != Direction.DOWN):
            self.snakeDirection = Direction.UP
        if (pyxel.btn(pyxel.KEY_S)==True and self.snakeDirection != Direction.UP):
            self.snakeDirection = Direction.DOWN
        if (pyxel.btn(pyxel.KEY_A)==True and self.snakeDirection != Direction.RIGHT):
            self.snakeDirection = Direction.LEFT
        if (pyxel.btn(pyxel.KEY_D)==True and self.snakeDirection != Direction.LEFT):
            self.snakeDirection = Direction.RIGHT
            

    def draw(self):
        pyxel.cls(1)
        self.coin.draw()
        for s in self.snake:
            s.draw(self.snakeDirection)
            
    def moveSnake(self):
        
        checkPosition = False
        
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
            
            if s == self.snake[0]: 
                if self.coin.IsColliding(s):
                    self.addSection()
                    self.coin.randomPosition() 
                    checkPosition = True
                    self.snakeSpeed += (self.snakeSpeed * 0.1)
                continue
            
            currentLocationX = s.x
            currentLocationY = s.y
            
            s.x = previousLocationX
            s.y = previousLocationY
            
            previousLocationX = currentLocationX
            previousLocationY = currentLocationY
            
            if self.coin.IsColliding(s) and checkPosition:
                self.coin.randomPosition()
        
    def addSection(self):
        if self.snakeDirection == Direction.RIGHT:
            self.snake.append(SnakeSection(self.snake[-1].x - self.snake[-1].w, self.snake[-1].y))
        if self.snakeDirection == Direction.LEFT:
            self.snake.append(SnakeSection(self.snake[-1].x + self.snake[-1].w, self.snake[-1].y))
        if self.snakeDirection == Direction.UP:
            self.snake.append(SnakeSection(self.snake[-1].x, self.snake[-1].y - self.snake[-1].h))
        if self.snakeDirection == Direction.DOWN:
            self.snake.append(SnakeSection(self.snake[-1].x, self.snake[-1].y + self.snake[-1].h))
        #min 45:39
App(WIDTH,HEIGHT)
        