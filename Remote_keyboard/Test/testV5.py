import pygame
import time
from pygame.locals import *
from sys import exit
pygame.init()
def print_key():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
			   exit()
			if event.type == KEYDOWN:
				#键盘有按下？
				#if event.key == K_LEFT:
				if event.key == K_a:
					print("a")
				#elif event.key == K_RIGHT:
				elif event.key == K_d:
					print("d")

				#elif event.key == K_UP:
				elif event.key == K_w:
					print("w")
					
				#elif event.key == K_DOWN:
				elif event.key == K_s:
					print("s")

			elif event.type == KEYUP:
				#如果用户放开了键盘
				print(0)
			time.sleep(0.01)

 
