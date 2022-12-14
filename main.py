import pygame
from pygame.locals import *
import constants
import time
import random
from pygame import mixer



class apple():
    def __init__(self,parent_window):
        self.parent_window=parent_window
        self.image=pygame.image.load("apple.png")
        self.x=120
        self.y=120
    def draw(self):
        self.parent_window.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.x=random.randint(24,776)
        self.y=random.randint(24,576)




class snake():
    def __init__(self,parent_window,lenght):
        self.parent_window=parent_window
        self.snake_body=pygame.image.load("image\circle.png")
        self.direction="right"
        self.lenght=lenght
        self.x=[24]*lenght
        self.y=[24]*lenght
    def increase_lenght(self):
        self.lenght +=1
        self.x.append(-1)
        self.y.append(-1)
    def draw(self):
        self.parent_window.fill(constants.BG_COLOR) 
        for i in range(self.lenght):   
            self.parent_window.blit(self.snake_body,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'
            movement=mixer.Sound("sounds\ss.wav")
            movement.play(0)  
    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'
            movement=mixer.Sound("sounds\ss.wav")
            movement.play(0)  
    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'
            movement=mixer.Sound("sounds\ss.wav")
            movement.play(0)  
    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down' 
            movement=mixer.Sound("sounds\ss.wav")
            movement.play(0)                         
           
       
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
        pygame.mixer.music.load("sounds\8-bit-game-music-122259.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        

        pygame.display.update()

    def is_colision(self,x1,y1,x2,y2):
        if x1 >=x2 and x1<x2 + constants.SNAKE_BODY:
            if y1>=y2 and y1<y2 + constants.SNAKE_BODY:
                return True
        return False            
    def play(self):
        self.snake.walk()
        self.apple.draw() 
        self.display_score()
        pygame.display.flip()
        if self.is_colision(self.snake.x[0], self.snake.y[0], self.apple.x,self.apple.y):
            mordisco=mixer.Sound("sounds\coin.wav")
            mordisco.play()
            self.snake.increase_lenght()
            constants.score+=1    
            self.apple.move()  

        for i in range(3,self.snake.lenght):
            if self.is_colision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                

                self.show_game_over()
    def show_game_over(self):
        font = pygame.font.Font("dd.ttf",44)
        message1=font.render(f"Game over, tu puntaje es {constants.score}",True,(54, 21, 96 ))
        self.window.blit(message1,(10,200))
        message2=font.render(f"presiona enter para continuar o esc salir",True,(54, 21, 96 ))
        self.window.blit(message2,(10,250))
        choque=mixer.Sound("sounds\hurt_c_08-102842.wav")
        choque.play()
        pygame.display.flip()

                    

           

    def display_score(self):
        font=pygame.font.Font("dd.ttf",44)
        score=font.render(f'score:{constants.score}',True,(21, 96, 55 ))
        self.window.blit(score,(10,10))






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
            self.play()
            time.sleep(0.1)               
game=Game()
game.run()

