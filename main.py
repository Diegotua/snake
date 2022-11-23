import pygame
from pygame.locals import *
import constants


class Game():
    def __init__(self):
        pygame.init
        self.window=pygame.display.set_mode(constants.SIZE)
        self.title=pygame.display.set_caption(constants.TITLE)
        icon=pygame.image.load("image\snakes.png")
        pygame.display.set_icon(icon)
        self.window.fill(constants.BG_COLOR)
        pygame.display.update()

    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                elif event.type==QUIT:
                    running=False        
game=Game()
game.run()

