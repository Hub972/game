#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
import sys
import time
import os

# Load the level and add 3 objects under random position
pygame.init()


def make_level():
    with open("level.txt", "r") as file:
        build_level = [list(line) for line in file.read().split("\n")]
    for i in range(3):
        while True:
            x = random.randint(0, 14)
            y = random.randint(0, 14)
            if not build_level[x][y] in ("1", "2", "3", "4", "5", "6"):
                build_level[x][y] = i + 4
                break
    return build_level


def find_player(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "3":
                return i, j


# Make a new position for '3' if it don't '1' and return a new platform
def right(build_level):
    maze = build_level[:]
    x, y = find_player(maze)
    if y < 14:
        if maze[x][y+1] != "1":
            maze[x][y+1] = "3"
            maze[x][y] = "0"
    return maze


def left(build_level):
    maze = build_level[:]
    x, y = find_player(maze)
    if y > 0:
        if maze[x][y-1] != "1":
            maze[x][y-1] = "3"
            maze[x][y] = "0"
    return maze


def up(build_level):
    maze = build_level[:]
    x, y = find_player(maze)
    if x > 0:
        if maze[x-1][y] != "1":
            maze[x-1][y] = "3"
            maze[x][y] = "0"
    return maze


def down(build_level):
    maze = build_level[:]
    x, y = find_player(maze)
    if x < 14:
        if maze[x+1][y] != "1":
            maze[x+1][y] = "3"
            maze[x][y] = "0"
    return maze


# Take the platform and blit each picture for each condition
def make_graph(maze):
    screen = pygame.display.set_mode((450, 450))
    frame = pygame.image.load("media/oc.png")
    frame = pygame.transform.scale(frame, (450, 450))
    media = os.listdir("media")
    name = ["guard", "lframe", "mac", "ether", "wall", "pipe", "syring"]
    a = 0
    for i in media:
        name[a] = pygame.image.load("media/" + i)
        a += 1
    screen.blit(frame, (0, 0))
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
            elif sprite == 4:
                screen.blit(name[5], (x, y))
            elif sprite == 5:
                screen.blit(name[6], (x, y))
            elif sprite == 6:
                screen.blit(name[3], (x, y))
            num_case += 1
        num_line += 1
    pygame.display.set_caption('MacGame')
    pygame.display.flip()
    return


# For each position of '3' check if the condition is done or wrong
def result_game(maze):
    count_ob = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "3":
                x_ply = i
                y_ply = j
            elif maze[i][j] == 4 or maze[i][j] == 5 or maze[i][j] == 6:
                count_ob += 1
    if maze[x_ply][y_ply] == maze[14][14]:
        if count_ob == 0:
            pygame.display.set_caption("You win")
            time.sleep(5)
            sys.exit(0)
        else:
            pygame.display.set_caption('You lose')
            time.sleep(3)
            sys.exit(0)


# Set the game
d = ""
build = make_level()
make_graph(build)

# Launch the game
while d != "q":
    # Check the events with pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            d = "q"
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                maze = right(build)
                make_graph(maze)
                result_game(maze)
            elif event.key == K_LEFT:
                maze = left(build)
                make_graph(maze)
                result_game(maze)
            elif event.key == K_DOWN:
                maze = down(build)
                make_graph(maze)
                result_game(maze)
            elif event.key == K_UP:
                maze = up(build)
                make_graph(maze)
                result_game(maze)
