import pygame
import sys
import os
#from config import *


# Window Configs
WIN_WIDTH = 800
WIN_HEIGHT = 600

DEBUG = False

FPS = 60

TILE_SIZE = 32

# Temp Variables
TEMP1 = 50 # Debug max times

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

# Other
pygame.init()
SCREEN = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT), flags=0, depth=32, vsync=0)
pygame.display.set_caption('ASTEROIDS Fangame v0.1.4 Alpha')
pygame.display.set_icon(pygame.image.load('sprites/icon.png'))
#pygame.mouse.set_visible(False)
CLOCK = pygame.time.Clock()


# Functions
def drawText(_screen, _text, _color, _size, _pos):
	TEMP_FONT = pygame.font.Font(None, _size)
	TEMP_REN = TEMP_FONT.render(_text, False, _color, None)
	TEMP_RECT = TEMP_REN.get_rect()
	TEMP_RECT.center = ((_pos[0] * 2) / 2, (_pos[1] * 2) / 2)
	_screen.blit(TEMP_REN, TEMP_RECT)


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

	def update(self):
		pass


	def draw(self):
		pass


# Main Functions
def mainMenu():
	global DEBUG, COUNTER0

	# Variables
	mainRun = True

	option_selected = 0

	# Objects
	test1 = testObject(400, 300)

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

				if event.key == pygame.K_UP:
					print('UP')

				if event.key == pygame.K_DOWN:
					print('DOWN')

		# Update Objects
		test1.update()

		# Drawn Objects
		test1.draw()

		# Drawn GUI
		drawText(SCREEN, 'PLAY', WHITE, 26, (WIN_WIDTH / 2, (WIN_HEIGHT / 2) - 15))
		drawText(SCREEN, 'MORE', WHITE, 26, (WIN_WIDTH / 2, (WIN_HEIGHT / 2) + 15))

		drawText(SCREEN, 'Version 0.1.4', WHITE, 20, (WIN_WIDTH / 2, WIN_HEIGHT - 60))
		drawText(SCREEN, 'by LeyfoGazel', WHITE, 20, (WIN_WIDTH / 2, WIN_HEIGHT - 40))

		# End Code

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
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_p:
					DEBUG = not DEBUG

		# Drawn Objects

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