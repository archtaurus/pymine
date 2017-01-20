#!/usr/bin/env python
# -*- coding: utf-8 -*-
# block.py
"""
Block
A class definition for the block in the game PyMine.
"""
import pygame
from pygame.locals import *
from lib.mixer import *

block_image = {
    0: pygame.image.load('resource/image/0.png'),
    1: pygame.image.load('resource/image/1.png'),
    2: pygame.image.load('resource/image/2.png'),
    3: pygame.image.load('resource/image/3.png'),
    4: pygame.image.load('resource/image/4.png'),
    5: pygame.image.load('resource/image/5.png'),
    6: pygame.image.load('resource/image/6.png'),
    7: pygame.image.load('resource/image/7.png'),
    8: pygame.image.load('resource/image/8.png'),
    "block": pygame.image.load('resource/image/block.png'),
    "flag": pygame.image.load('resource/image/flag.png'),
    "mine": pygame.image.load('resource/image/mine.png'),
    "boom": pygame.image.load('resource/image/boom.png'),
    "wrong": pygame.image.load('resource/image/wrong.png')}


class Block(object):

    def __init__(self, minefield, mined):
        self.minefield = minefield
        self.mined = mined
        self.digged = False
        self.flagged = False
        self.image = block_image["block"]
        self.rect = Rect(0, 0, 0, 0)
        self.ambient_blocks = []
        self.number_of_ambient_mines = 0
        self.number_of_ambient_flags = 0

    def render(self, image_name = None):
        if image_name in block_image.keys():
            self.image = block_image[image_name]
        self.minefield.background.blit(self.image, self.rect)

    def click(self, button):
        if button == 1 and not self.digged:
            self.dig()
        elif button == 1 and self.digged:
            self.dig_around()
        elif button == 3:
            self.stick_flag()

    def stick_flag(self):
        if not self.digged:
            self.flagged = not self.flagged
            play_sound("flag", 1)
            if self.flagged:
                self.render("flag")
                for block in self.ambient_blocks:
                    block.number_of_ambient_flags += 1
            else:
                self.render("block")
                for block in self.ambient_blocks:
                    block.number_of_ambient_flags -= 1

    def dig(self):
        if not self.digged and not self.flagged:
            self.digged = True
            play_sound("dig", 2)
            if self.mined:
                self.render("boom")
                play_sound("boom", 3)
                self.minefield.loss()
            else:
                self.render(self.number_of_ambient_mines)
                self.minefield.number_of_digged_blocks += 1
                if self.minefield.number_of_digged_blocks == self.minefield.number_of_safe_blocks:
                    self.minefield.win()
                if self.number_of_ambient_mines == 0 or self.number_of_ambient_flags == self.number_of_ambient_mines:
                    for block in self.ambient_blocks:
                        block.dig()

    def dig_around(self):
        if self.digged and self.number_of_ambient_mines > 0 and self.number_of_ambient_flags == self.number_of_ambient_mines:
            for block in self.ambient_blocks:
                block.dig()
