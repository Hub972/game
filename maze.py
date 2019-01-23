#! /usr/bin/env python3
# -*- coding: utf8 -*-
import random
import pygame
from pygame.locals import *

pygame.init()


class Maze:
    def __init__(self):
        self.maze = []
        self.build_level = []
        self.tile = ""

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

    def find_mac(self, maze):
        """Check the position of mac"""
        self.maze = maze
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == "3":
                    return i, j
        return None

    def find_tile(self, maze, tile):
        self.maze = maze
        self.tile = tile
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == self.tile:
                    return i, j
        return None

    @classmethod
    def right(cls, build_level):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = cls.find_mac(cls, cls.maze)
        if y < 14:
            if cls.maze[x][y + 1] != "1":
                cls.maze[x][y + 1] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def left(cls, build_level):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = cls.find_mac(cls, cls.maze)
        if y > 0:
            if cls.maze[x][y - 1] != "1":
                cls.maze[x][y - 1] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def up(cls, build_level):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = cls.find_mac(cls, cls.maze)
        if x > 0:
            if cls.maze[x - 1][y] != "1":
                cls.maze[x - 1][y] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def down(cls, build_level):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = cls.find_mac(cls, cls.maze)
        if x < 14:
            if cls.maze[x + 1][y] != "1":
                cls.maze[x + 1][y] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    def component_found(self, maze):
        """Check if the component is under the maze"""
        self.maze = maze
        x_p, y_p = self.find_mac(self.maze)
        if self.maze[x_p][y_p] == self.maze[14][14]:
            if self.find_tile(self.maze, "4") or self.find_tile(self.maze, "5") or self.find_tile(self.maze, "6"):
                return "check victory..."
        pass

    def blit_picture(self, pictures, maze):
        """Blit all the pictures on the maze"""
        self.maze = maze
        self.pictures = pictures
        screen = pygame.display.set_mode((450, 450))
        screen.blit(self.pictures["00"], (0, 0))
        for n_line, line in enumerate(self.maze):
            for n_tile, tile in enumerate(line):
                x = n_tile * 30
                y = n_line * 30
                if tile != "0": screen.blit(self.pictures[tile], (x, y))
