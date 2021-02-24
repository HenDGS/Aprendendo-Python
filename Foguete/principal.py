import sys
import pygame
import eventos as inp
from settings import *
from foguete import *

def run_game():
	pygame.init()
	config=Settings()
	screen=pygame.display.set_mode((config.screen_width,config.screen_height))
	pygame.display.set_caption("Mars Simulator")	
	foguete=Ship(screen,config.speed)
	
	while True:
		inp.check_event(foguete)
		foguete.update()
		inp.update_screen(config,screen,foguete)
			
		screen.fill(config.cor_fundo)
		foguete.blitme()
			
		pygame.display.flip()
		
run_game()

