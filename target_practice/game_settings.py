class Settings:
	"""A Class to store all settings for Target Practice."""

	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5

		# Bullet settings
		self.bullet_speed = 2
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (255, 10, 10)

		# target Settings
		self.target_speed = 1
		self.target_direction = 1
	