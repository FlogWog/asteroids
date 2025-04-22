import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
    
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group, updatable, drawable)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # below is the game loop
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
             if asteroid.collision(player):
                  print("Game over!")
                  sys.exit()
             for shot in shots_group:
                  if shot.collision(asteroid):
                       shot.kill()
                       asteroid.split()
        shots_group.update(dt)
        screen.fill("black")
        for object in drawable:
             object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000











if __name__ == "__main__":
        main()