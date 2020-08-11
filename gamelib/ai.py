from gamelib.game import *
from time import time as timer


def key(left=0,right=0,jump=0):
	return {'left':left,'right':right,'jump':jump}



# ============
class ai():
	def __init__(self):
		self.game = None

	def loop_game(self):
		while True:
			self.game.main_loop(key())

	def ai_game_manager(self, screen, level):
		# slow settings
		slow_movement_speed = 2
		slow_const_jump_speed = -6.4

		# fast settings
		fast_movement_speed = 3
		fast_const_jump_speed = -9

		self.game = Game(screen,self,level,movement_speed=fast_movement_speed,const_jump_speed=fast_const_jump_speed)

		self.level = level

	def move_right(self,seconds = 1):
		print("Moving right for {} seconds".format(seconds))
		init_t = timer()
		while(timer() - init_t < seconds):
			self.game.main_loop(key(right=True))
	
	def move_left(self,seconds = 1):
		print("Moving left for {} seconds".format(seconds))
		init_t = timer()
		
		while(timer() - init_t < seconds):
			self.game.main_loop(key(left=True))

	def jump(self):
		print("Jumping")
		init_t = timer()
		while(timer() - init_t < 0.2):
			self.game.main_loop(key(jump=True))

	def jump_right(self):
		print("Jumping right")
		init_t = timer()
		while(timer() - init_t < 0.2):
			self.game.main_loop(key(right=True ,jump=True))
		while(timer() - init_t < 0.8):
			self.game.main_loop(key(right=True))

	def jump_left(self):
		print("Jumping left")
		init_t = timer()
		while(timer() - init_t < 0.2):
			self.game.main_loop(key(left=True))

		while(timer() - init_t < 0.8):
			self.game.main_loop(key(left=True ,jump=True))

	def wait(self, seconds= 1):
		print("Waiting for {} seconds".format(seconds))
		seconds = 1
		init_t = timer()
		while(timer() - init_t < seconds):
			self.game.main_loop(key())


	def start_game(self, game):
		self.game = game
		init_t = timer()
		while(timer() - init_t < 2):
			self.game.main_loop(key())
		self.ai_instructions()

	# ====================================================
	# =============== AI functions go here ===============

	def sample_ai(self):
		self.move_right(seconds=2)
		self.jump_right()
		self.jump()
		self.wait(seconds=2)
		self.move_left()
		self.jump_left()
		self.wait(seconds=3)

	def jump_forever(self):
		while True:
			self.jump()


	def move_and_jump_5_times(self):
		for i in range(5):
			self.move_right()
			self.jump_right()

	def walk_right_jump_when_approaching_enemy(self):
		while(True):
			if (self.game.player.mario_sees_enemy):
				self.jump_right()
			else:
				self.move_right(0.1)

	# ====================================================


	def ai_instructions(self):
		print("AI begins")

		# ============================================
		# =============== AI goes here ===============
		self.move_and_jump_5_times()

		print("AI ends")
		# ============================================

		self.loop_game()
		







# ================================ 
# ================================ 

# avaliable levels:
# lvl 1: hallway
# lvl 2: stairs
# lvl 3: stairs with a hole
# lvl 4: two enemiess, then stairs with a hole
# lvl 5: two enemiess, then stairs with a hole, then another enemy

# you can edit levels by editing lvl_edu_x.png files