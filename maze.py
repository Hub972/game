#! /usr/bin/env python3
# -*- coding: utf8 -*-
import random
import pygame
from pygame.locals import *

pygame.init()


class Maze:
    def __init__(self):
        self.build_level = Maze.make_level()
        self.count = 0
        self.maze = self.build_level[:]

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

    def find_mac(self):
        """Check the position of mac"""
        return self.find_tile("3")

    def find_tile(self, tile):
        """Check the position about the tile in parameter"""
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == tile:
                    return i, j
        return None

    def right(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if y < 14:
            if self.maze[x][y + 1] != "1":
                self.maze[x][y + 1] = "3"
                self.maze[x][y] = "0"
        print(self.maze)

    def left(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if y > 0:
            if self.maze[x][y - 1] != "1":
                self.maze[x][y - 1] = "3"
                self.maze[x][y] = "0"

    def up(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if x > 0:
            if self.maze[x - 1][y] != "1":
                self.maze[x - 1][y] = "3"
                self.maze[x][y] = "0"

    def down(self):
        """Make a new position for '3' if it don't '1'"""
        x, y = self.find_mac()
        if x < 14:
            if self.maze[x + 1][y] != "1":
                self.maze[x + 1][y] = "3"
                self.maze[x][y] = "0"

    def component_count(self):
        """Check the count of component"""
        cnt = 0
        for i in range(len(self.maze)):
            for y in range(len(self.maze[i])):
                if self.maze[i][y] == "4" or self.maze[i][y] == "5" or self.maze[i][y] == "6":
                    cnt += 1
        self.count = cnt


    def component_found(self):
        """Check if the component is under the maze"""
        if self.find_tile("4") or self.find_tile("5") or self.find_tile("6"):
            return True
        pass

    def blit_picture(self, pictures):
        """Blit all the pictures on the maze"""
        ORANGE = 255, 100, 0  # color for the text
        text = pygame.font.SysFont('freesans', 13)  # Police and size
        screen = pygame.display.set_mode((450, 450))  # Set the size' screen
        screen.blit(pictures["00"], (0, 0))  # Picture for the font
        """Loop for blit all the pictures"""
        for n_line, line in enumerate(self.maze):
            for n_tile, tile in enumerate(line):
                x = n_tile * 30
                y = n_line * 30
                if tile != "0": screen.blit(pictures[tile], (x, y))
        """Set the rect for the counter in the screen"""
        self.component_count()
        title_text = text.render("Number of object(s) to found: {}".format(self.count),
                                 True, ORANGE)
        textpos = title_text.get_rect()
        textpos.centerx = 350
        textpos.centery = 10
        screen.blit(title_text, textpos)
        pygame.display.flip()

    def check_pos(self):
        """Check if mac is on the guard"""
        x_p, y_p = self.find_mac()
        print(x_p, y_p)
        if self.maze[x_p][y_p] == self.maze[14][14]:
            return True
        pass

    def draw(self, pictures):
        """All the methode for draw in 'game' """
        self.blit_picture(pictures)
        self.component_count()
