import pygame as pg
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FRAMES_PER_SECOND

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    fps_timer = pg.time.Clock()
    dt = 0
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pg.display.flip()
        dt = fps_timer.tick(FRAMES_PER_SECOND) / 1000

if __name__ == "__main__":
    main()