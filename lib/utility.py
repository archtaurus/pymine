#!/usr/bin/env python
# -*- coding: utf-8 -*-
# utility.py
"""
Utility
Module for the other functions for the game PyMine.
"""
import pygame
from pygame.locals import *


def render_text(text, surface, position, font, color, align = "topleft"):
    text_render = font.render(text, True, color)
    if align == "topleft":
        text_position = position
    elif align == "center":
        text_position = text_render.get_rect()
        text_position.center = position
    surface.blit(text_render, text_position)


class MyMouse:

    def __init__(self, image_filename):
        self.cursor = pygame.image.load(image_filename)
        self.rect = self.cursor.get_rect()
        pygame.mouse.set_visible(0)

    def render(self, surface):
        self.rect = pygame.mouse.get_pos()
        surface.blit(self.cursor, self.rect)

    def set_image(self, image):
        self.cursor = image
        self.rect = image.get_rect()


def _test():
    from sys import exit
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), 0, 32)

    def test_render_text():
        pygame.display.set_caption("utility -> _test() -> test_render_text()")
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont('Airal', 60)
        render_text("Hello World!", screen, font, (0, 0, 0), (320, 240), "center")
        pygame.display.flip()
        while get_input() != "next":
            pass

    def test_MyMouse():
        pygame.display.set_caption("utility -> _test() -> test_MyMouse()")
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont('Airal', 60)
        mouse = MyMouse('../resource/image/shovel.png')
        pygame.mouse.set_visible(0)
        while get_input() != "next":
            screen.fill((255, 255, 255))
            render_text("Hello World!", screen, font, (0, 0, 0), (320, 240), "center")
            mouse.render(screen)
            pygame.display.flip()

    def get_input():
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_n:
                    return "next"

    test_render_text()
    test_MyMouse()

if __name__ == "__main__":
    _test()
