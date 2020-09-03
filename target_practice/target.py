import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent target"""

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the target image and set rect attribute.
		self.image = pygame.image.load('images/mario.bmp')
		self.rect = self.image.get_rect()

		# Start the target at right of screen
		self.rect.midright = self.screen_rect.midright

		# Store a decimal value for the target's vertical position
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Return True if target hits edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True
