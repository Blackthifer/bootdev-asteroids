import pygame as pg
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_ACCELERATION, PLAYER_DECELERATION, SCREEN_HEIGHT, SCREEN_WIDTH

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

    def accelerate(self, dt, forward = 1):
        #forward should be 1 or -1
        self.velocity += pg.Vector2(0,1).rotate(self.rotation) * PLAYER_ACCELERATION * dt * forward

    def update(self, dt):
        self.handle_input(dt)
        self.position += self.velocity
        self.screenwrap()
        self.velocity *= PLAYER_DECELERATION

    def screenwrap(self):
        if self.position.x <= -PLAYER_RADIUS:
            self.position.x = SCREEN_WIDTH + PLAYER_RADIUS
        elif self.position.x >= SCREEN_WIDTH + PLAYER_RADIUS:
            self.position.x = -PLAYER_RADIUS
        if self.position.y <= -PLAYER_RADIUS:
            self.position.y = SCREEN_HEIGHT + PLAYER_RADIUS
        elif self.position.y >= SCREEN_HEIGHT + PLAYER_RADIUS:
            self.position.y = -PLAYER_RADIUS
    
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