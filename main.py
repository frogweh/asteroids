import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame
import constants

def main():
    print(f"Starting asteroids!\nScreen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")    

if __name__ == "__main__":
    main()
