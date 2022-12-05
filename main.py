import pygame
from pygame.locals import *
import constants
import time
import random

class apple():
    def __init__(self,parent_window):
        self.parent_window=parent_window
        self.image=pygame.image.load("apple.png")
        self.x=120
        self.y=120
    def draw(self):
        self.parent_window.blit(self.image,(self.x,self.y))
        pygame.display.flip()



class snake():
    def __init__(self,parent_window,lenght):
        self.parent_window=parent_window
        self.snake_body=pygame.image.load("image\circle.png")
        self.direction="right"
        self.lenght=lenght
        self.x=[24]*lenght
        self.y=[24]*lenght
    def draw(self):
        self.parent_window.fill(constants.BG_COLOR) 
        for i in range(self.lenght):   
            self.parent_window.blit(self.snake_body,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction="left"
        
    def move_right(self):
        self.direction="right"
        
    def move_up(self):
        self.direction="up"
        
    def move_down(self):
        self.direction="down"
           
       
    def walk(self):
        for i in range(self.lenght-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=="left":
            self.x[0]-=constants.SNAKE_BODY
        if self.direction=="right":
            self.x[0]+=constants.SNAKE_BODY    
        if self.direction=="up":
            self.y[0]-=constants.SNAKE_BODY
        if self.direction=="down":
            self.y[0]+=constants.SNAKE_BODY
        self.draw()
class Game():

    def __init__(self):
        pygame.init()        
        self.window=pygame.display.set_mode(constants.SIZE)
        self.title=pygame.display.set_caption(constants.TITLE)
        icon=pygame.image.load("image\snakes.png")
        pygame.display.set_icon(icon)
        self.window.fill(constants.BG_COLOR)
        self.snake=snake(self.window,4)
        self.snake.draw()
        self.apple=apple(self.window,)
        self.apple.draw()

        pygame.display.update()

    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False                                                
                    if event.key ==K_LEFT:
                        self.snake.move_left()

                    if event.key ==K_RIGHT:
                        self.snake.move_right()

                    if event.key ==K_UP:
                        self.snake.move_up()  

                    if event.key ==K_DOWN:
                        self.snake.move_down()                
                elif event.type==QUIT:
                    running=False 

            self.snake.walk()
            self.apple.draw()
            time.sleep(0.1)               
game=Game()
game.run()

