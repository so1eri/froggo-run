from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from sys import exit
from frog import Frog
from vinegar import Vinegar

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("froggo run")
clock = pygame.time.Clock()
cooldown = False
font = pygame.font.Font(None, 16)
Drawing = pygame.image.load('Drawing.png')
Drawing = pygame.transform.smoothscale_by(Drawing, 0.153)

vinegar = Vinegar()
frog = Frog()

def main():
  while True:
    handle_events()
    update()
    draw()

def handle_events():
  global cooldown
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        frog.velocity = -7
    if event.type == USEREVENT:
      cooldown = False

def update():
  global cooldown
  clock.tick(FPS)
  frog.update()
  vinegar.update()
  if frog.mask.overlap(vinegar.mask1, ( vinegar.x - 40, 0 - frog.y)):
    if not cooldown:
      frog.lives -=1
      pygame.time.set_timer(USEREVENT, 1000, loops = 1)
      cooldown = True

  if frog.mask.overlap(vinegar.mask2, ( vinegar.x - 40, vinegar.y - frog.y)):
    if not cooldown:
      frog.lives -=1
      pygame.time.set_timer(USEREVENT, 1000, loops = 1)
      cooldown = True


def draw():
  screen.fill((0,0,0))
  screen.blit(font.render("lives: " + str(frog.lives), False, (255, 255, 255)),(0, 0))
  screen.blit(font.render("score: " + str(vinegar.score + frog.lives - 3), False, (255, 255, 255)),(0, 20))
  frog.draw(screen)
  vinegar.draw(screen)
  if frog.lives < 1:
    screen.blit(Drawing, (0, 0))
  pygame.display.flip()

main()


#PROBLEM 1 frog can double jump
#PROBLEM 2 vinegar only spawns once  