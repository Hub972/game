import pygame
from pygame.locals import *
import game
import maze as dr


pygame.init()


def main():
    """Set the game"""
    d = ""
    gam = game.Game()
    direc = dr.Maze()
    build = direc.make_level()
    pic = gam.load_media()
    gam.draw(pic, build)

    """Launch the game"""
    while d != "q":
        """Check the events with pygame"""
        for event in pygame.event.get():
            if event.type == QUIT:
                d = "q"
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    maze = direc.right(build)
                    gam.draw(pic, maze)
                    gam.check_victory(maze)
                elif event.key == K_LEFT:
                    maze = direc.left(build)
                    gam.draw(pic, maze)
                    gam.check_victory(maze)
                elif event.key == K_DOWN:
                    maze = direc.down(build)
                    gam.draw(pic, maze)
                    gam.check_victory(maze)
                elif event.key == K_UP:
                    maze = direc.up(build)
                    gam.draw(pic, maze)
                    gam.check_victory(maze)


if __name__ == '__main__':
    main()
