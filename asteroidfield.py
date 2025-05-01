import pygame as pg
import random as rand
from asteroid import Asteroid
from constants import *

class AsteroidField(pg.sprite.Sprite):
    edges = [
            lambda y: pg.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
            lambda y: pg.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
            lambda x: pg.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
            lambda x: pg.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS),
            ]

    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.spawn_timer = 0
    
    def update(self, dt):
        self.spawn_timer += dt
        rand.seed()
        if self.spawn_timer >= ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            
            edge = rand.choice(self.edges)
            position = edge(rand.uniform(0, 1))
            velocity = pg.Vector2(1, 0).rotate(rand.randrange(360)) * rand.normalvariate(40, 10)
            radius = rand.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
            Asteroid(position.x, position.y, velocity.x, velocity.y, radius)