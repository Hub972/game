#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import time
from maze import Maze

pygame.init()


class Game:
    def __init__(self):
        self.pictures = Game.load_media()
        self.maze = Maze()

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

    def draw(self):
        """Draw the graphique maze"""
        self.maze.draw(self.pictures)
        pygame.display.set_caption("Welcome to the MacGame")
        pygame.display.flip()

    def run(self):
        """Set the game"""
        d = ""
        self.draw()
        """Launch the game"""
        while d != "q":
            """Check the events with pygame"""
            for event in pygame.event.get():
                if event.type == QUIT:
                    d = "q"
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.maze.move_right()
                        self.draw()
                        self.check_victory()
                    elif event.key == K_LEFT:
                        self.maze.move_left()
                        self.draw()
                        self.check_victory()
                    elif event.key == K_DOWN:
                        self.maze.move_down()
                        self.draw()
                        self.check_victory()
                    elif event.key == K_UP:
                        self.maze.move_up()
                        self.draw()
                        self.check_victory()

    def check_victory(self):
        """For each position of mac check if the condition is done or wrong."""
        if self.maze.check_final_condition():
            if self.maze.component_found():
                pygame.display.set_caption('You lose')
                time.sleep(3)
                sys.exit(0)
            else:
                pygame.display.set_caption("You win")
                time.sleep(3)
                sys.exit(0)


