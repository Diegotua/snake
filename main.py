import pygame
from pygame.locals import *
import constants


class snake():
    def __init__(self,parent_window):
        self.parent_window=parent_window
        self.snake_body=pygame.image.load("image\circle.png")
        self.x=600
        self.y=300
    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)    
        self.parent_window.blit(self.snake_body,(self.x,self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -=10
        self.draw()
    def move_right(self):
        self.x +=10
        self.draw()
    def move_up(self):
        self.y-=10
        self.draw()
    def move_down(self):
        self.y+=10 
        self.draw()   




class Game():

    def __init__(self):
        pygame.init()        
        self.window=pygame.display.set_mode(constants.SIZE)
        self.title=pygame.display.set_caption(constants.TITLE)
        icon=pygame.image.load("image\snakes.png")
        pygame.display.set_icon(icon)
        self.window.fill(constants.BG_COLOR)
        self.snake=snake(self.window)
        self.snake.draw()

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
game=Game()
game.run()

