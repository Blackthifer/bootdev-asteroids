import pygame as pg
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    pg.key.set_repeat(16)
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    fps_timer = pg.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    update_objects = [player]

    while True:
        for object in update_objects:
            object.update(dt)
        screen.fill("black")
        player.draw(screen)
        pg.display.flip()
        dt = fps_timer.tick(FRAMES_PER_SECOND) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return

if __name__ == "__main__":
    main()