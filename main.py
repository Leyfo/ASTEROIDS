import pygame
import sys
import os
import random
import math
#from config import *


# Window Configs
WIN_WIDTH = 800
WIN_HEIGHT = 600

DEBUG = False

FPS = 60

TILE_SIZE = 32

# Temp Variables
TEMP1 = 50 # Debug max times
TEMP_TEXT_PLAY = 'PLAY'
TEMP_TEXT_EXIT = 'EXIT'

# For Loops
COUNTER0 = 100 # Debug
COUNTER1 = 0
COUNTER2 = 0
COUNTER3 = 0
COUNTER4 = 0
COUNTER5 = 0
COUNTER6 = 0
COUNTER7 = 0
COUNTER8 = 0
COUNTER9 = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CYAN = (0, 255, 255)
PINK = (255, 0, 255)
YELLOW = (255, 255, 0)

# Custom Colors
SCREEN_COLOR_ALPHA = (20,20,20)

# Import sound effects
#snd_fire = pygame.mixer.Sound("sounds/fire.wav")
#snd_bangL = pygame.mixer.Sound("sounds/bangLarge.wav")
#snd_bangM = pygame.mixer.Sound("sounds/bangMedium.wav")
#snd_bangS = pygame.mixer.Sound("sounds/bangSmall.wav")
#snd_extra = pygame.mixer.Sound("sounds/extra.wav")
#snd_saucerB = pygame.mixer.Sound("sounds/saucerBig.wav")
#snd_saucerS = pygame.mixer.Sound("sounds/saucerSmall.wav")


# Functions
def drawText(_screen, _text, _color, _size, _pos):
	TEMP_FONT = pygame.font.Font(None, _size)
	TEMP_REN = TEMP_FONT.render(_text, False, _color, None)
	TEMP_RECT = TEMP_REN.get_rect()
	TEMP_RECT.center = ((_pos[0] * 2) / 2, (_pos[1] * 2) / 2)
	_screen.blit(TEMP_REN, TEMP_RECT)


def loadImg(_pathFile):
	return pygame.image.load(_pathFile)


# Classes
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.x = x
		self.y = y


	def update(self):
		pass


	def draw(self):
		pass


class testObject(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = loadImg('sprites/err.png')
		self.angle = 0
		self.speed = 0
		self.maxSpeed = 10

	def isColliding(self, _x, _y, _xTo, _yTo, _size):
		if _x > _xTo - _size and _x < _xTo + _size and _y > _yTo - _size and _y < _yTo + _size:
			return True
		return False

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			if self.speed <= self.maxSpeed: self.speed += 1
		if keys[pygame.K_DOWN]:
			if self.speed <= self.maxSpeed: self.speed -= 1
		if keys[pygame.K_LEFT]:
			self.angle += 1
		if keys[pygame.K_RIGHT]:
			self.angle -= 1

		angle_rad = math.radians(self.angle)

		self.x += -self.speed * math.sin(angle_rad)
		self.y += self.speed * math.cos(angle_rad)

	def draw(self):
		TEMP_IMG_PLAYER = pygame.transform.rotate(self.image, self.angle)
		SCREEN.blit(TEMP_IMG_PLAYER, (self.x - int(TEMP_IMG_PLAYER.get_width() / 2), self.y - int(TEMP_IMG_PLAYER.get_height() / 2)))


# Other
pygame.init()
SCREEN = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT), flags=0, depth=32, vsync=0)
pygame.display.set_caption('ASTEROIDS Fangame v0.1.4 Alpha')
pygame.display.set_icon(loadImg('sprites/icon.png'))
#pygame.mouse.set_visible(False)
CLOCK = pygame.time.Clock()


# Main Functions
def mainMenu():
	global DEBUG, COUNTER0, TEMP_TEXT_PLAY, TEMP_TEXT_MORE, TEMP_TEXT_EXIT

	# Variables
	mainRun = True

	option_selected = 0

	# Objects
	#test1 = testObject(400, 300)

	while mainRun:

		SCREEN.fill(SCREEN_COLOR_ALPHA) # Clear Screen

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # stop game button
				mainRun = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					mainRun = False
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_p:
					DEBUG = not DEBUG

				if event.key == pygame.K_x:
					if option_selected == 0:
						mainRun = False
						game()

					if option_selected == 1:
						mainRun = False
						pygame.quit()
						sys.exit()

				if event.key == pygame.K_UP:
					if option_selected == 1: option_selected = 0

				if event.key == pygame.K_DOWN:
					if option_selected == 0: option_selected = 1

		# Update Objects
		#test1.update()

		# Drawn Objects
		#test1.draw()

		# Drawn GUI
		TEMP_TEXT_PLAY = 'PLAY'
		TEMP_TEXT_EXIT = 'EXIT'

		if option_selected == 0:
			TEMP_TEXT_PLAY = '- PLAY -'
		if option_selected == 1:
			TEMP_TEXT_EXIT = '- EXIT -'

		drawText(SCREEN, TEMP_TEXT_PLAY, WHITE, 26, (WIN_WIDTH / 2, (WIN_HEIGHT / 2) - 15))
		drawText(SCREEN, TEMP_TEXT_EXIT, WHITE, 26, (WIN_WIDTH / 2, (WIN_HEIGHT / 2) + 15))

		drawText(SCREEN, 'Version 0.1.4', WHITE, 20, (WIN_WIDTH / 2, WIN_HEIGHT - 60))
		drawText(SCREEN, 'by LeyfoGazel', WHITE, 20, (WIN_WIDTH / 2, WIN_HEIGHT - 40))

		# End Code

		if DEBUG:
			drawText(SCREEN, str(f"FPS: {int(CLOCK.get_fps())}"), WHITE, 20, (30, 20))

		if COUNTER0 >= TEMP1 and DEBUG:
			COUNTER0 = 0

			print('\n-- DEBUG --')
			print('SCREEN: ' + str(SCREEN))
			print('CLOCK: ' + str(CLOCK))
		else:
			COUNTER0 = COUNTER0 + 1

		pygame.display.update()
		CLOCK.tick(FPS) / 1000


def game():

	global DEBUG, COUNTER0

	gameRun = True

	test1 = testObject(400, 300)
	test1.image = loadImg('sprites/nave.png')

	while gameRun:

		SCREEN.fill(SCREEN_COLOR_ALPHA) # Clear Screen

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # stop game button
				gameRun = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameRun = False
					mainMenu()

				if event.key == pygame.K_p:
					DEBUG = not DEBUG

		# Update Objects
		test1.update()
		#test1.angle += 1

		# Drawn Objects
		test1.draw()

		# Drawn GUI

		# End Code

		if COUNTER0 >= TEMP1 and DEBUG:
			COUNTER0 = 0

			print('SCREEN: ' + str(SCREEN))
			print('CLOCK: ' + str(CLOCK))
		else:
			COUNTER0 = COUNTER0 + 1

		pygame.display.update()
		CLOCK.tick(FPS) / 1000


# Start
mainMenu()
