#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
import sys
import time
import os
import direction

pygame.init()


# Load the level and add 3 objects under random position
def make_level():
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
    media = os.listdir("media")
    name = ["guard", "frame", "mac", "ether", "wall", "pipe", "syring"]
    a = 0
    for i in media:
        name[a] = pygame.image.load("media/" + i)
        a += 1
    return name


# Take the platform and blit each picture for each condition
def draw(maze, name):
    screen = pygame.display.set_mode((450, 450))
    name[1] = pygame.transform.scale(name[1], (450, 450))
    screen.blit(name[1], (0, 0))
    num_line = 0
    for line in maze:
        num_case = 0
        for sprite in line:
            x = num_case * 30
            y = num_line * 30
            if sprite == "1":
                screen.blit(name[4], (x, y))
            elif sprite == "3":
                screen.blit(name[2], (x, y))
            elif sprite == "2":
                screen.blit(name[0], (x, y))
            elif sprite == "4":
                screen.blit(name[5], (x, y))
            elif sprite == "5":
                screen.blit(name[6], (x, y))
            elif sprite == "6":
                screen.blit(name[3], (x, y))
            num_case += 1
        num_line += 1
    pygame.display.set_caption('MacGame')
    pygame.display.flip()


# For each position of '3' check if the condition is done or wrong.
def result_game(maze):
    x, y = direction.find_player(maze)
    if maze[x][y] == maze[14][14]:
        count_ob = 0
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if "4" in maze[i][j] or "5" in maze[i][j] or "6" in maze[i][j]:
                    count_ob += 1
        if count_ob == 0:
            pygame.display.set_caption('You win')
            time.sleep(3)
            sys.exit(0)
        else:
            pygame.display.set_caption("You lose")
            time.sleep(5)
            sys.exit(0)


# Set the game
d = ""
build = make_level()
direc = direction.Mac(build)
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
                result_game(maze)
            elif event.key == K_LEFT:
                maze = direc.left(build)
                draw(maze, name)
                result_game(maze)
            elif event.key == K_DOWN:
                maze = direc.down(build)
                draw(maze, name)
                result_game(maze)
            elif event.key == K_UP:
                maze = direc.up(build)
                draw(maze, name)
                result_game(maze)
