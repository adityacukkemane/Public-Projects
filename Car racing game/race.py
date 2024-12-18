import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

car_img = pygame.image.load('car.png')
car_width = car_img.get_width()

obstacle_img = pygame.image.load('obstacle.png')
obstacle_width = obstacle_img.get_width