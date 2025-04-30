import pygame as pg
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    fps_timer = pg.time.Clock()
    dt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        pg.display.flip()
        dt = fps_timer.tick(FRAMES_PER_SECOND) / 1000


if __name__ == "__main__":
    main()