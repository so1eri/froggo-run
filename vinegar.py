import pygame
from random import randint
vinegar = pygame.image.load('vinegar.png')


class Vinegar:
  def __init__(self):
    self.tepelort()
    self.score = 0
  def tepelort(self):
    self.height = randint(-89, 89)
    self.image1 = pygame.transform.smoothscale(vinegar, (103, 90+self.height))
    self.image2 = pygame.transform.smoothscale(vinegar, (103, 90-self.height))
    self.mask1 = pygame.mask.from_surface(self.image1)
    self.mask2 = pygame.mask.from_surface(self.image2)

    self.x = 600

  def draw(self, screen):
    screen.blit(self.image1, (self.x,0))
    screen.blit(self.image2, (self.x,self.y))

    # self.mask1.to_surface(screen, dest = (self.x, 0))
    # self.mask2.to_surface(screen, dest = (self.x, self.y))


  def update(self):
    self.y = 210+self.height
    self.x -= 5
    if self.x < 0:
      self.tepelort()
      self.score += 1
      print(self.score)

