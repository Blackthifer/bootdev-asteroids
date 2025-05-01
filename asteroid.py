import pygame as pg
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, pos_x, pos_y, vel_x, vel_y, radius):
        super().__init__(pos_x, pos_y, radius)
        self.velocity = pg.math.Vector2(vel_x, vel_y)
    
    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.screenwrap()

    def screenwrap(self):
        if self.position.x <= -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x >= SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y <= -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y >= SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius    
