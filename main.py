import pygame
from pygame.locals import *
import game
import maze


pygame.init()


def main():
    """Set the game"""
    d = ""
    gam = game.Game()
    mz = maze.Maze()
    t = mz.make_level()
    gam.load_media()
    gam.draw(t)

    """Launch the game"""
    while d != "q":
        """Check the events with pygame"""
        for event in pygame.event.get():
            if event.type == QUIT:
                d = "q"
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    new_maze = mz.right()
                    gam.draw(new_maze)
                    gam.check_victory()
                elif event.key == K_LEFT:
                    new_maze = mz.left()
                    gam.draw(new_maze)
                    gam.check_victory()
                elif event.key == K_DOWN:
                    new_maze = mz.down()
                    gam.draw(new_maze)
                    gam.check_victory()
                elif event.key == K_UP:
                    new_maze = mz.up()
                    gam.draw(new_maze)
                    gam.check_victory()


if __name__ == '__main__':
    main()
