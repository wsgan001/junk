#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import pi

WIDTH = 800				# main window width
HEIGHT = 700			# main window height

SPEED_OF_EATER = 200	# max speed of eaters
SPEED_OF_FOOD = 0		# max speed of food

CNT_EATERS = 10			# number of eaters
CNT_FOOD = 10			# number of food

CNT_INPUT_FOOD = 6
CNT_INPUT_EATERS = 2

EAT_DISTANCE = 10.0		# расстояние, на котором пожиратель может съесть еду
VISUAL_ANGLE = pi  		# угол зрения, под которым пожиратели видят еду (и других пожирателей)

MAX_FOOD = 10 			# на каком количестве съеденной пищи запускается генетический алгоритм

TIME_TO_RESET = 60.0	# через сколько секунд обновить положение игроков на экране
