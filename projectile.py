import pygame
from circleshape import CircleShape
from constants import PROJECTILE_RADIUS,PROJECTILE_COLOR

class Projectile(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PROJECTILE_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen,PROJECTILE_COLOR,self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt