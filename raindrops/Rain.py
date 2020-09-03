import sys
import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	"""Class to represent a single rain"""
	def __init__(self, ai_game):
		"""initialize rain and set start position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load raom image and set its rect
		self.image = pygame.image.load('rain.bmp')
		self.rect = self.image.get_rect()

		# Start each new rain near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the rain horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update(self):
		"""Move Rain down and slightly diagonally across screen"""
		self.y += 1
		self.x += 0.2
		self.rect.x = self.x
		self.rect.y = self.y
		

class Raining:
	"""Overall class to manage rain"""
	
	def __init__(self):
		"""Initialize the screen and resources"""
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)	
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		self.bg_color = (255, 255, 255)
		pygame.display.set_caption("Raining")
		
		self.raindrops = pygame.sprite.Group()
		self.raindrop_height = 110
		self._create_raindrops()
	
	def run_game(self):
		"""Start the programme and display raindrops"""
		while True:
			self._check_events()
			self._update_rain()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypress for quit"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

	def _create_raindrops(self):
		"""create multiple stars"""
		raindrop = Rain(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		available_space_x = self.screen_width - (2 * raindrop_width)
		number_raindrops_x = available_space_x // (2 * raindrop_width)

		#Determine number of rows of stars that fit on screen.
		self.screen_height = self.screen.get_rect().height
		raindrop_height = self.raindrop_height
		available_space_y = (self.screen_height - (3 * raindrop_height) - raindrop_height)
		number_rows = available_space_y // (raindrop_height)
		

		# create full screen of stars.
		for row_number in range(number_rows):
			for raindrops_number in range(number_raindrops_x):

				self._create_rain(raindrops_number, row_number)

	def _create_rain(self, raindrops_number, row_number):
		"""Create star and place it in row"""
		raindrop = Rain(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		raindrop.x = raindrop_width + 2 * raindrop_width * raindrops_number
		raindrop.rect.y = raindrop.rect.height + 2 * self.raindrop_height * (row_number + 1)	
		self.raindrops.add(raindrop)

	def _update_rain(self):
		"""Update the position of all raindrop on screen"""
		self._check_rain_edges()
		self.raindrops.update()


	def _check_rain_edges(self):
		"""Respond to rain hitting bottom"""
		self.screen_height = self.screen.get_rect().height
		for rain in self.raindrops.copy():
			if rain.rect.bottom >= self.screen_height:
				self.raindrops.remove(rain)
				self._create_raindrops()
			break

				

	def _update_screen(self):
		"""Update images on the screen adn flip new screen"""
		self.screen.fill(self.bg_color)
		self.raindrops.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = Raining()
	ai.run_game()
