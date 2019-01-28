#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import time
import maze

pygame.init()


class Game:
    def __init__(self):
        self.maze = maze.Maze()

    def draw(self):
        self.maze.blit_picture()
        # pygame.display.flip()

    """def draw(self, maze):
        ""Draw the graphique maze""
        self.maze.draw(self.picture, maze)
        #self.maze.component_count()
        pygame.display.flip()"""

    def check_victory(self):
        """For each position of mac check if the condition is done or wrong."""
        if self.maze.check_pos():
            if self.maze.component_found():
                pygame.display.set_caption('You lose')
                time.sleep(3)
                sys.exit(0)
            else:
                pygame.display.set_caption("You win")
                time.sleep(3)
                sys.exit(0)
