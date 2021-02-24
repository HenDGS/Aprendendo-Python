import pygame
import sys

def check_event(nave):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				nave.moving_right=True
			elif event.key==pygame.K_LEFT:
				nave.moving_left=True
			elif event.key==pygame.K_UP:
				nave.moving_up=True
			elif event.key==pygame.K_DOWN:
				nave.moving_down=True
		
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				nave.moving_right=False
			elif event.key==pygame.K_LEFT:
				nave.moving_left=False
			elif event.key==pygame.K_UP:
				nave.moving_up=False
			elif event.key==pygame.K_DOWN:
				nave.moving_down=False
	
	
			
def update_screen(config,screen,nave):
		screen.fill(config.cor_fundo)
		nave.blitme()
			
		pygame.display.flip()
		
	

