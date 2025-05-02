import pygame as pg
import random as rand
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

    def split(self, shot_rotation):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle_deviation = rand.uniform(40, 90)
            vel1 = self.velocity.rotate(angle_deviation) * ASTEROID_SPLIT_SPEED_MULT
            vel2 = self.velocity.rotate(-angle_deviation) * ASTEROID_SPLIT_SPEED_MULT
            new_radius = self.radius // 2
            Asteroid(self.position.x, self.position.y, vel1.x, vel1.y, new_radius)
            Asteroid(self.position.x, self.position.y, vel2.x, vel2.y, new_radius)
        self.kill()
            

    def screenwrap(self):
        if self.position.x <= -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x >= SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y <= -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y >= SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius    
