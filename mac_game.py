#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
import sys
import time
import direction as dr

pygame.init()


def make_level():
    # Load the level and add 3 objects under random position
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


def load_media():
    # Load all pictures necessary
    pictures = {}
    for tile, name in (("2", "Guardien"), ("00", "oc"), ("3", "MacGyver"), ("6", "ether"), ("1", "wall"), ("4", "pipe"), \
                       ("5", "syring")):
        pictures[tile] = pygame.image.load("media/" + name + ".png")
    pictures["00"] = pygame.transform.scale(pictures["00"], (450, 450))
    return pictures


def draw(maze, pictures):
    # Take the platform and blit each picture for each condition
    screen = pygame.display.set_mode((450, 450))
    screen.blit(pictures["00"], (0, 0))
    for n_line, line in enumerate(maze):
        for n_tile, tile in enumerate(line):
            x = n_tile * 30
            y = n_line * 30
            if tile != "0": screen.blit(pictures[tile], (x, y))
    pygame.display.set_caption('MacGame')
    pygame.display.flip()


def check_victory(maze):
    # For each position of '3' check if the condition is done or wrong.
    x_p, y_p = dr.find_tile(maze, "3")
    if maze[x_p][y_p] == maze[14][14]:
        if dr.find_tile(maze, "4") or dr.find_tile(maze, "5") or dr.find_tile(maze, "6"):
            pygame.display.set_caption('You lose')
            time.sleep(3)
            sys.exit(0)
        else:
            pygame.display.set_caption("You win")
            time.sleep(3)
            sys.exit(0)


def main():
    # Set the game
    d = ""
    build = make_level()
    direc = dr.Mac(build)
    name = load_media()
    draw(build, name)

    # Launch the game
    while d != "q":
        # Check the events with pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                d = "q"
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    maze = direc.right(build)
                    draw(maze, name)
                    check_victory(maze)
                elif event.key == K_LEFT:
                    maze = direc.left(build)
                    draw(maze, name)
                    check_victory(maze)
                elif event.key == K_DOWN:
                    maze = direc.down(build)
                    draw(maze, name)
                    check_victory(maze)
                elif event.key == K_UP:
                    maze = direc.up(build)
                    draw(maze, name)
                    check_victory(maze)


if __name__ == '__main__':
    main()
