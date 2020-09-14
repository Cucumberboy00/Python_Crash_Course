import pygame
from pygame.sprite import Sprite

class Target(Sprite):
	"""A class to represent target"""

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

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

	def center_target(self):
		# Start the target at right of screen
		self.rect.midright = self.screen_rect.midright

		# Store a decimal value for the target's vertical position
		self.y = float(self.rect.y)

	def update(self):
		"""Move the target up &/or down."""
		self.y += (self.settings.target_speed *
					self.settings.target_direction)
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

