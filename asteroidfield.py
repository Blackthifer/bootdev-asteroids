import pygame as pg
import random as rand
from asteroid import Asteroid
from constants import *

class AsteroidField(pg.sprite.Sprite):
    edges = [
            lambda y, r: pg.Vector2(-r, y * SCREEN_HEIGHT),
            lambda y, r: pg.Vector2(SCREEN_WIDTH + r, y * SCREEN_HEIGHT),
            lambda x, r: pg.Vector2(x * SCREEN_WIDTH, -r),
            lambda x, r: pg.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + r),
            ]

    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.spawn_timer = 0
    
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            
            radius = rand.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
            edge = rand.choice(self.edges)
            position = edge(rand.uniform(0, 1), radius)
            velocity = pg.Vector2(1, 0).rotate(rand.randrange(360)) * rand.normalvariate(40, 10)
            Asteroid(position.x, position.y, velocity.x, velocity.y, radius)