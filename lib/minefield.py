#!/usr/bin/env python
# -*- coding: utf-8 -*-
# minefield.py
"""
Minefield
A class definition for the minefield in the game PyMine.
"""
from random import shuffle
import pygame
from pygame.locals import *
from lib.utility import render_text
from lib.block import *
from lib.mixer import *


class Minefield(object):

    def __init__(self, columns, rows):
        self.number_of_columns, self.number_of_rows = columns, rows
        self.font_color = (200, 0, 0)
        self.size_of_block = 20
        load_music("bgm")
        self.new()

    def new(self):
        stop_sound()
        self.font_size = min(self.number_of_columns, self.number_of_rows) * 2
        self.font = pygame.font.Font('resource/font/acknowtt.ttf', self.font_size)
        self.number_of_blocks = self.number_of_columns * self.number_of_rows
        self.number_of_mines = self.number_of_blocks // 6
        self.number_of_safe_blocks = self.number_of_blocks - self.number_of_mines
        self.size_of_window = (self.size_of_block * self.number_of_columns, self.size_of_block * self.number_of_rows)
        self.screen = pygame.display.set_mode(self.size_of_window, 0, 32)
        self.background = pygame.surface.Surface(self.size_of_window, 0, 32)
        self.blocks, self.mined_blocks = [], []
        for i in range(self.number_of_mines):
            new_block = Block(self, 1)
            self.blocks.append(new_block)
            self.mined_blocks.append(new_block)
        for i in range(self.number_of_safe_blocks):
            new_block = Block(self, 0)
            self.blocks.append(new_block)
        self.number_of_digged_blocks = 0
        shuffle(self.blocks)
        for n in range(self.number_of_blocks):
            if (n % self.number_of_columns) == 0:
                for i in [n + 1, n - self.number_of_columns, n - self.number_of_columns + 1, n + self.number_of_columns, n + self.number_of_columns + 1]:
                    if i in range(self.number_of_blocks):
                        self.blocks[n].ambient_blocks.append(self.blocks[i])
                        self.blocks[n].number_of_ambient_mines += self.blocks[i].mined
            elif (n % self.number_of_columns) == (self.number_of_columns - 1):
                for i in [n - 1, n - self.number_of_columns - 1, n - self.number_of_columns, n + self.number_of_columns - 1, n + self.number_of_columns]:
                    if i in range(self.number_of_blocks):
                        self.blocks[n].ambient_blocks.append(self.blocks[i])
                        self.blocks[n].number_of_ambient_mines += self.blocks[i].mined
            else:
                for i in [n + 1, n - 1, n - self.number_of_columns - 1, n - self.number_of_columns, n - self.number_of_columns + 1, n + self.number_of_columns - 1, n + self.number_of_columns, n + self.number_of_columns + 1]:
                    if i in range(self.number_of_blocks):
                        self.blocks[n].ambient_blocks.append(self.blocks[i])
                        self.blocks[n].number_of_ambient_mines += self.blocks[i].mined
            column = n % self.number_of_columns
            row = n // self.number_of_columns
            x = self.size_of_block * column
            y = self.size_of_block * row
            self.blocks[n].rect = Rect(x, y, self.size_of_block, self.size_of_block)
            self.blocks[n].render("block")
        play_music()
        self.state = "playing"

    def click(self, position, button):
        if self.state == "playing":
            (x, y) = position
            n = (x // self.size_of_block) + self.number_of_columns * (y // self.size_of_block)
            self.blocks[n].click(button)

    def win(self):
        if self.state == "playing":
            self.state = "win"
            stop_music()
            play_sound("win", 0)
            for block in self.mined_blocks:
                block.flaged = True
                block.render("flag")
            render_text("YOU WIN", self.background, self.background.get_rect().center, self.font, self.font_color, "center")

    def loss(self):
        if self.state == "playing":
            self.state = "loss"
            stop_music()
            play_sound("loss", 0)
            for block in self.blocks:
                if block.flagged:
                    if not block.mined:
                        block.render("wrong")
                elif block.mined and not block.digged:
                    block.render("mine")
            render_text("GAME OVER", self.background, self.background.get_rect().center, self.font, self.font_color, "center")

    def render(self):
        self.screen.blit(self.background, (0, 0))
