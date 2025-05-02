import pygame as pg
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    
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

    def accelerate(self, dt, forward = 1):
        #forward should be 1 or -1
        self.velocity += pg.Vector2(0,1).rotate(self.rotation) * PLAYER_ACCELERATION * dt * forward

    def update(self, dt):
        self.shot_cooldown -= dt
        self.handle_input(dt)
        self.position += self.velocity
        self.screenwrap()
        self.velocity *= PLAYER_DECELERATION

    def shoot(self):
        shot_position = self.position + pg.Vector2(0,1).rotate(self.rotation) * PLAYER_RADIUS
        Shot(shot_position.x, shot_position.y, self.rotation)

    def screenwrap(self):
        if self.position.x <= -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x >= SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y <= -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y >= SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
    
    def handle_input(self, dt):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_d] or pressed[pg.K_RIGHT]:
            self.rotate(dt, 1)
        if pressed[pg.K_a] or pressed[pg.K_LEFT]:
            self.rotate(dt, -1)
        if pressed[pg.K_w] or pressed[pg.K_UP]:
            self.accelerate(dt, 1)
        if pressed[pg.K_s] or pressed[pg.K_DOWN]:
            self.accelerate(dt, -1)
        if (pressed[pg.K_SPACE] or pressed[pg.K_j]) and self.shot_cooldown <= 0:
            self.shot_cooldown = SHOT_DELAY
            self.shoot()