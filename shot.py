import pygame as pg
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pg.Vector2(0, 1).rotate(rotation) * SHOT_SPEED

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.y < -self.radius or self.position.y >= SCREEN_HEIGHT + self.radius or self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius:
            self.kill()