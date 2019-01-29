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
    mz.make_level()
    gam.load_media()
    gam.draw()

    """Launch the game"""
    while d != "q":
        """Check the events with pygame"""
        for event in pygame.event.get():
            if event.type == QUIT:
                d = "q"
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mz.right()
                    gam.draw()
                    gam.check_victory()
                elif event.key == K_LEFT:
                    mz.left()
                    gam.draw()
                    gam.check_victory()
                elif event.key == K_DOWN:
                    mz.down()
                    gam.draw()
                    gam.check_victory()
                elif event.key == K_UP:
                    mz.up()
                    gam.draw()
                    gam.check_victory()


if __name__ == '__main__':
    main()
