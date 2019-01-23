#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import time
import maze as dr

pygame.init()


class Game:
    def __init__(self):
        self.pictures = {}

    def load_media(self):
        """Load all pictures necessary"""
        for tile, name in (
        ("2", "Guardien"), ("00", "oc"), ("3", "MacGyver"), ("6", "ether"), ("1", "wall"), ("4", "pipe"),
        ("5", "syring")):
            self.pictures[tile] = pygame.image.load("media/" + name + ".png")
        self.pictures["00"] = pygame.transform.scale(self.pictures["00"], (450, 450))
        return self.pictures

    def draw(self, pictures, maze):
        """Draw the graphique maze"""
        self.maze = maze
        self.pictures = pictures
        blit_pic = dr.Maze()
        blit_pic.blit_picture(self.pictures, self.maze)
        blit_pic.component_count(self.maze)
        pygame.display.flip()

    def check_victory(self, maze):
        """For each position of mac check if the condition is done or wrong."""
        self.maze = list(maze)
        vic = dr.Maze()
        x_p, y_p = vic.find_mac(self.maze)
        if self.maze[x_p][y_p] == self.maze[14][14]:
            if vic.component_found(self.maze):
                pygame.display.set_caption('You lose')
                time.sleep(3)
                sys.exit(0)
            else:
                pygame.display.set_caption("You win")
                time.sleep(3)
                sys.exit(0)


