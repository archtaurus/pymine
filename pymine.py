#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""PyMine
    This is a minesweeper game, written in Python and with pygame."""

from sys import exit
import pygame
from pygame.locals import *
from lib.utility import MyMouse
from lib.minefield import Minefield

__filename__ = "pymine.py"
__title__ = 'PyMine'
__author__ = 'Zhao Xin (zhaoxin@imzhao.com)'
__copyright__ = 'Copyright 2013 Zhao Xin'
__licence__ = 'GPL'
__version__ = '0.6.0'

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("PyMine")
pymine_icon = pygame.image.load("resource/image/mine.png")
pygame.display.set_icon(pymine_icon)
mymouse = MyMouse('resource/image/shovel.png')
min_of_columns, max_of_columns = 10, 40
min_of_rows, max_of_rows = 10, 30
minefield = Minefield(min_of_columns, min_of_rows)

while True:
    clock.tick(60)
    minefield.render()
    mymouse.render(minefield.screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in [K_r, K_a, K_d, K_w, K_s]:
                if event.key == K_a:
                    minefield.number_of_columns = max(
                        min_of_columns, minefield.number_of_columns - 1)
                elif event.key == K_d:
                    minefield.number_of_columns = min(
                        max_of_columns, minefield.number_of_columns + 1)
                elif event.key == K_w:
                    minefield.number_of_rows = max(
                        min_of_rows, minefield.number_of_rows - 1)
                elif event.key == K_s:
                    minefield.number_of_rows = min(
                        max_of_rows, minefield.number_of_rows + 1)
                minefield.new()
        elif event.type == MOUSEBUTTONDOWN:
            minefield.click(event.pos, event.button)
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
