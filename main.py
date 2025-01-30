import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Projectile

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    Asteroid.containers = (updateable,drawable,asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable,drawable)
    Projectile.containers = (updateable,drawable,projectiles)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                return
            for bullet in projectiles:
                if asteroid.collision_check(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()