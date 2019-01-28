import pygame
from pygame.locals import *
import maze



pygame.init()


def main():
    """Set the game"""
    d = ""
    maz = maze.Maze()
    maz.make_level()
    maz.load_media()
    maz.blit_picture()

    """Launch the game"""
    while d != "q":
        """Check the events with pygame"""
        for event in pygame.event.get():
            if event.type == QUIT:
                d = "q"
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    maz.right()
                    maz.blit_picture()
                    maz.check_victory()
                elif event.key == K_LEFT:
                    maz.left()
                    maz.blit_picture()
                    maz.check_victory()
                elif event.key == K_DOWN:
                    maz.down()
                    maz.blit_picture()
                    maz.check_victory()
                elif event.key == K_UP:
                    maz.up()
                    maz.blit_picture()
                    maz.check_victory()


if __name__ == '__main__':
    main()
