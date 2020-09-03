import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
	"""Class to represent a single star"""
	def __init__(self, ai_game):
		"""initialize star and set start position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load star image and set its rect
		self.image = pygame.image.load('star.bmp')
		self.rect = self.image.get_rect()

		# Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the star horizontal position.
		self.x = float(self.rect.x)



class Stars:
	"""Overall class to manage stars"""
	
	def __init__(self):
		"""Initialize the screen and resources"""
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)	
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		self.bg_color = (0, 0, 0)
		pygame.display.set_caption("Stars")
		
		self.stars = pygame.sprite.Group()
		self._create_stars()
	
	def run_game(self):
		"""Start the programme and display stars"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypress for quit"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

	def _create_stars(self):
		"""create multiple stars"""
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = self.screen_width - (2 * star_width)
		number_stars_x = available_space_x // (2 * star_width)

		#Determine number of rows of stars that fit on screen.
		available_space_y = (self.screen_height - (3 * star_height) - star_height)
		number_rows = available_space_y // (star_height)

		# create full screen of stars.
		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
		"""Create star and place it in row"""
		star = Star(self)
		
		star_width, star_height = star.rect.size
		star.x = star_width + 2 * star_width * star_number
		random_number = randint(-50, 50)
		star.rect.x = star.x + random_number
		random_number = randint(-50, 50) 
		star.rect.y = star.rect.height + 2 * star.rect.height * row_number + random_number
		self.stars.add(star)

	def _update_screen(self):
		"""Update images on the screen adn flip new screen"""
		self.screen.fill(self.bg_color)
		self.stars.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = Stars()
	ai.run_game()
