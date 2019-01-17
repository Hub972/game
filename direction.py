#! /usr/bin/env python3
# -*- coding: utf8 -*-


# Check the position of mac
def find_tile(maze, tile):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == tile:
                return i, j
    return None


class Mac:
    def __init__(self, build_level):
        self.build_level = build_level

    # Make a new position for '3' if it don't '1' and return a new platform
    @classmethod
    def right(cls, build_level):
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = find_tile(cls.maze, "3")
        if y < 14:
            if cls.maze[x][y + 1] != "1":
                cls.maze[x][y + 1] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def left(cls, build_level):
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = find_tile(cls.maze, "3")
        if y > 0:
            if cls.maze[x][y - 1] != "1":
                cls.maze[x][y - 1] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def up(cls, build_level):
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = find_tile(cls.maze, "3")
        if x > 0:
            if cls.maze[x - 1][y] != "1":
                cls.maze[x - 1][y] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)

    @classmethod
    def down(cls, build_level):
        cls.build_level = build_level
        cls.maze = cls.build_level[:]
        x, y = find_tile(cls.maze, "3")
        if x < 14:
            if cls.maze[x + 1][y] != "1":
                cls.maze[x + 1][y] = "3"
                cls.maze[x][y] = "0"
        return list(cls.maze)
