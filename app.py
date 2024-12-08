#!/usr/bin/env python3

import pygame

print(pygame.init())
print(pygame.get_init())


#Set Size, by default not resizable. 
#To make window resizable, use pygame.display.set_mode((960,540), pygame.RESIZABLE)
screen = pygame.display.set_mode((960,540))

#Get Size
print(screen.get_size())

#Set Title
pygame.display.set_caption('this is a title')

#Set Icon
icon = pygame.image.load('snakeIcon.png')
pygame.display.set_icon(icon)

#Set Surface Color using RBG
color = (255,0,255)
screen.fill(color)
pygame.display.flip()


#Draw a rectange
pygame.draw.rect(screen, "blue", pygame.Rect(300,300,50,50))

pygame.display.flip()

#Make sure the game keeps running until quit
gameRuns = True
while gameRuns:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			gameRuns = False
