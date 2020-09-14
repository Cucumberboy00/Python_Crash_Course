import sys

import pygame

from game_settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target
from button import Button

class TargetPractice:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Target Practice")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)
		self.hitcount = 0

		self.play_button = Button(self, "Play")

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			if self.settings.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_target()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)	
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)	

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE and self.settings.game_active:
			self._fire_bullet()
		elif event.key == pygame.K_p and not self.settings.game_active:
			self._start_game()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to to key Releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.settings.game_active:
			self._start_game()

	def _start_game(self):
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)
		# Reset the game statistics/
		self.settings.game_active = True

		# Get rid of any remaining bullets & reset hitcount.
		self.bullets.empty()
		# Create a new fleet and center the ship.
		self.target.center_target()
		self.ship.center_ship()
		self.settings.initialize_dynamic_settings()

	def _fire_bullet(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()

		# Get rid of bullets that have dissapeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.screen.get_rect().width:
				self.bullets.remove(bullet)
				self.settings.misses += 1
				if self.settings.misses >= 3:
					self.settings.game_active = False
					pygame.mouse.set_visible(True)
					self.hitcount = 0
					self.settings.misses = 0
					break
			bullet.draw_bullet()

		self._check_bullet_target_collisions()

	def _check_bullet_target_collisions(self):
		"""Respond to bullet-target collisions."""
		# Check for any bullets that have hit target.
		#    If so, get rid of the bullet keep the target.
		for bullet in self.bullets.copy():
			if bullet.is_collided_with(self.target):
				bullet.kill()
				self.hitcount +=1
				print("Good Hit #" + str(self.hitcount))
				if self.hitcount % 3 == 0:
					self.settings.increase_speed() 

	def _update_target(self):
		"""
		Check if the fleet is at an edge,
		 then Update the positions of all aliens in the fleet."""
		self._check_target_edges()
		self.target.update()
			
		
	def _check_target_edges(self):
		"""Respond if target hits edge"""
		if self.target.check_edges():
			self._change_target_direction()

	def _change_target_direction(self):
		self.settings.target_direction *= -1

	def _update_screen(self):
		"""Update images on the screen, and flip to new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.target.blitme()

		# Draw the play button if the game is inactive.
		if not self.settings.game_active:
			self.play_button.draw_button()

		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = TargetPractice()
	ai.run_game()

		