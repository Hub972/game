#! /usr/bin/env python3
# -*- coding: utf8 -*-

import random
import pygame
from pygame.locals import *

pygame.init()


class Maze:
    def __init__(self):
        self.tiles = Maze.make_level()
        self.count = 0

    @staticmethod
    def make_level():
        """Load the level and add 3 objects under random position"""
        with open("level.txt", "r") as file:
            build_level = [list(line) for line in file.read().split("\n")]
        for i in range(3):
            while True:
                x = random.randint(0, 14)
                y = random.randint(0, 14)
                if not build_level[x][y] in ("1", "2", "3", "4", "5", "6"):
                    build_level[x][y] = str(i + 4)
                    break
        return build_level

    def find_tile(self, tile):
        """Check the position about the tile in parameter"""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == tile:
                    return i, j
        None

    def find_mac(self):
        """Check the position of mac"""
        return self.find_tile("3")

    def find_guard(self):
        """Check the position of the guardian"""
        return self.find_tile("2")

    def move_right(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if y < 14:
            if self.tiles[x][y + 1] != "1":
                self.tiles[x][y + 1] = "3"
                self.tiles[x][y] = "0"

    def move_left(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if y > 0:
            if self.tiles[x][y - 1] != "1":
                self.tiles[x][y - 1] = "3"
                self.tiles[x][y] = "0"

    def move_up(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if x > 0:
            if self.tiles[x - 1][y] != "1":
                self.tiles[x - 1][y] = "3"
                self.tiles[x][y] = "0"

    def move_down(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if x < 14:
            if self.tiles[x + 1][y] != "1":
                self.tiles[x + 1][y] = "3"
                self.tiles[x][y] = "0"

    def component_counter(self):
        """Check the count of component"""
        cnt = 0
        for i in range(len(self.tiles)):
            for y in range(len(self.tiles[i])):
                if self.tiles[i][y] == "4" or self.tiles[i][y] == "5" or self.tiles[i][y] == "6":
                    cnt += 1
        self.count = cnt

    def component_found(self):
        """Check if the component is under the maze"""
        return self.find_tile("4") or self.find_tile("5") or self.find_tile("6")

    def draw(self, pictures):
        """Blit all the pictures on the maze"""
        ORANGE = 255, 100, 0  # color for the text
        text = pygame.font.SysFont('freesans', 13)  # Police and size
        screen = pygame.display.set_mode((450, 450))  # Set the size' screen
        screen.blit(pictures["00"], (0, 0))  # Picture for the font
        """Loop for blit all the pictures"""
        for n_line, line in enumerate(self.tiles):
            for n_tile, tile in enumerate(line):
                x = n_tile * 30
                y = n_line * 30
                if tile != "0": screen.blit(pictures[tile], (x, y))
        """Set the rect for the counter in the screen"""
        self.component_counter()
        title_text = text.render("Number of object(s) to found: {}".format(self.count),
                                 True, ORANGE)
        textpos = title_text.get_rect()
        textpos.centerx = 350
        textpos.centery = 10
        screen.blit(title_text, textpos)
        pygame.display.flip()

    def check_final_condition(self):
        """Check if mac is on the guard"""
        return self.find_guard() is None

