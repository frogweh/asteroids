import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame
import constants
import circleshape
from player import player

def main():
    screen_width = constants.SCREEN_WIDTH
    screen_height = constants.SCREEN_HEIGHT
    player_object = player(screen_width / 2,screen_height / 2)
    print(f"Starting asteroids!\nScreen width: {screen_width}\nScreen height: {screen_height}")
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_object.update(dt)
        player_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
