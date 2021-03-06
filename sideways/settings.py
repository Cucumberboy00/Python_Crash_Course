class Settings:
	"""A Class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1900
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5
		self.ship_limit = 2

		# Bullet settings
		self.bullet_speed = 2
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		# Alien Settings
		self.alien_speed = 2
		self.fleet_drop_speed = 10
		# Fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1