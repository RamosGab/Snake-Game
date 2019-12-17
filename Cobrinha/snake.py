#To do:
#- Border collision with snake
#- Collision of the snake with itself
#- Punctuation
#- Put a background 

import pygame
from pygame.locals import *

import random
from random import randint


#Function to determine maximum apple size
def on_grid_random():
    x = random.randint(0 , 590)
    y = random.randint(0 , 590)
    return(x // 10 * 10, y // 10 * 10)

#border limits
# In progress
"""
def border_grid(borderx, bordery):
    x = borderx[0:591]
    y = bordery[0:591]
"""

#Function for collions between the apple and the snake
def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


#snake bump with the border
# In progress 
"""
def collision_border(c1, c2): 
"""

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3 

pygame.init()


#Screen Size
screenx = 600
screeny = 600
screen = pygame.display.set_mode((screenx,screeny))

pygame.display.set_caption('Snake - By Gabriel Ramos')

#Snake size, collor and initial position 
snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,0,255))


#Border building
#In progress
"""
border = pygame.Surface((10, 10 ))
border.fill((0,0,255))
border_position = 
"""

#Apple size, collor and initial position 
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_position = on_grid_random()


#Initial and automatic steering
my_direction = LEFT

#Funcion for fps
clock = pygame.time.Clock()

#Loop
while True:
    #Fps max 
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT    

    if collision(snake[0], apple_position):
        apple_position = on_grid_random()
        snake.append((0,0))
    
    

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i -1][0], snake[i-1][1])
 

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    
    screen.fill((0,0,0))
    screen.blit(apple,apple_position)
    for position in snake:
        screen.blit(snake_skin,position)
    
    pygame.display.update()
    