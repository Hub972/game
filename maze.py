#! /usr/bin/env python3
# -*- coding: utf8 -*-
import random
import time
import sys
import pygame
from pygame.locals import *

pygame.init()


class Maze:
    def __init__(self):
        self.pictures = Maze.load_media()
        self.build_level = Maze.make_level()
        self.count = int()
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

    @staticmethod
    def load_media():
        """Load all pictures necessary"""
        pictures = {}
        for tile, name in (
                ("2", "Guardien"), ("00", "oc"), ("3", "MacGyver"), ("6", "ether"), ("1", "wall"), ("4", "pipe"),
                ("5", "syring")):
            pictures[tile] = pygame.image.load("media/" + name + ".png")
        pictures["00"] = pygame.transform.scale(pictures["00"], (450, 450))
        return pictures

    def find_mac(self):
        """Check the position of mac"""
        return self.find_tile("3")

    def find_tile(self, tile):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == tile:
                    return i, j
        return None

    def right(self):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        x, y = self.find_mac()
        if y < 14:
            if self.maze[x][y + 1] != "1":
                self.maze[x][y + 1] = "3"
                self.maze[x][y] = "0"

    def left(self):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        x, y = self.find_mac()
        if y > 0:
            if self.maze[x][y - 1] != "1":
                self.maze[x][y - 1] = "3"
                self.maze[x][y] = "0"

    def up(self):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        x, y = self.find_mac()
        if x > 0:
            if self.maze[x - 1][y] != "1":
                self.maze[x - 1][y] = "3"
                self.maze[x][y] = "0"

    def down(self):
        """Make a new position for '3' if it don't '1' and return a new platform"""
        x, y = self.find_mac()
        if x < 14:
            if self.maze[x + 1][y] != "1":
                self.maze[x + 1][y] = "3"
                self.maze[x][y] = "0"

    def component_count(self):
        """"Check the count of component"""
        cnt = 0
        for i in range(len(self.maze)):
            for y in range(len(self.maze[i])):
                if self.maze[i][y] == "4" or self.maze[i][y] == "5" or self.maze[i][y] == "6":
                    cnt += 1
        self.count = cnt
        pygame.display.set_caption("Mac game")
        return  self.count

    def component_found(self):
        """Check if the component is under the maze"""
        x_p, y_p = self.find_mac()
        if self.maze[x_p][y_p] == self.maze[14][14]:
            if self.find_tile("4") or self.find_tile("5") or self.find_tile("6"):
                return True
        return False

    def blit_picture(self):
        """Blit all the pictures on the maze"""
        ORANGE = 255, 100, 0
        text = pygame.font.SysFont('freesans', 13)
        screen = pygame.display.set_mode((450, 450))
        screen.blit(self.pictures["00"], (0, 0))
        for n_line, line in enumerate(self.maze):
            for n_tile, tile in enumerate(line):
                x = n_tile * 30
                y = n_line * 30
                if tile != "0": screen.blit(self.pictures[tile], (x, y))
        self.component_count()
        title_text = text.render("Number of object(s) to found: {}".format(self.count),
                                 True, ORANGE)
        textpos = title_text.get_rect()
        textpos.centerx = 350
        textpos.centery = 10
        screen.blit(title_text, textpos)

        pygame.display.flip()

    def check_pos(self):
        x, y = self.find_mac()
        print(x, y)
        if self.maze[x][y] == self.maze[14][14]:
            return True

    def check_victory(self):
        """For each position of mac check if the condition is done or wrong."""
        if self.check_pos():
            if self.component_found():
                pygame.display.set_caption('You lose')
                time.sleep(3)
                sys.exit(0)
            else:
                pygame.display.set_caption("You win")
                time.sleep(3)
                sys.exit(0)
