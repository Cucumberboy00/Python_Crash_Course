class Settings:
	"""A Class to store all settings for Target Practice."""

	def __init__(self):
		"""Initialize game settings."""
		
		#Start Target Practice in an in-active state.
		self.game_active = False
		self.misses = 0

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (255, 10, 10)	

		# How quickly the game speeds up 
		self.speedup_scale = 2

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Intialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.target_speed = 1.0

		# target_direction of 1 represents right; -1 represents left.
		self.target_direction = 1

	def increase_speed(self):
		"""Increase speed settings."""
		self.target_speed *= self.speedup_scale