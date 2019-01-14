#! /usr/bin/env python3
# -*- coding: utf8 -*-


# Check the position of mac
def find_player(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "3":
                return i, j
            else:
                None


class Mac:
    def __init__(self, build_level):
        self.build_level = build_level

    # Make a new position for '3' if it don't '1' and return a new platform
    @classmethod
    def right(cls, build_level):
        cls.build_level = build_level
        maze = cls.build_level[:]
        x, y = find_player(maze)
        if y < 14:
            if maze[x][y + 1] != "1":
                maze[x][y + 1] = "3"
                maze[x][y] = "0"
        return list(maze)

    @classmethod
    def left(cls, build_level):
        cls.build_level = build_level
        maze = cls.build_level[:]
        x, y = find_player(maze)
        if y > 0:
            if maze[x][y - 1] != "1":
                maze[x][y - 1] = "3"
                maze[x][y] = "0"
        return list(maze)

    @classmethod
    def up(cls, build_level):
        cls.build_level = build_level
        maze = cls.build_level[:]
        x, y = find_player(maze)
        if x > 0:
            if maze[x - 1][y] != "1":
                maze[x - 1][y] = "3"
                maze[x][y] = "0"
        return list(maze)

    @classmethod
    def down(cls, build_level):
        cls.build_level = build_level
        maze = cls.build_level[:]
        x, y = find_player(maze)
        if x < 14:
            if maze[x + 1][y] != "1":
                maze[x + 1][y] = "3"
                maze[x][y] = "0"
        return list(maze)
