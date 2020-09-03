import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialize the alien and set its start position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top right of the screen.
		self.rect.bottomright = self.screen_rect.bottomright
	
		# Store the aliens Vertical Position.
		self.x = float(self.rect.x)

	def check_edges(self):
		screen_rect = self.screen_rect
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True

	def update(self):
		"""Move alien to the bottom"""
		self.y += (self.settings.alien_speed *
					self.settings.fleet_direction)
		self.rect.y = self.y


	def update_x(self):
		self.x += self.rect.width
		self.rect.x = self.x