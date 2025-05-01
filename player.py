import pygame as pg
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pg.Vector2(0,1).rotate(self.rotation)
        right = pg.Vector2(0,1).rotate(self.rotation + 90) / 1.5
        a = self.position + forward * self.radius
        b = self.position - (forward + right) * self.radius
        c = self.position - (forward - right) * self.radius
        return [a, b, c]
    
    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt, direction = 1):
        #direction should be 1 or -1
        self.rotation += PLAYER_TURN_SPEED * dt * direction

    def update(self, dt):
        pass