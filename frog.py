import pygame
frog = pygame.image.load('nugget froggo.png')
frog = pygame.transform.flip(frog, True, False)
frog = pygame.transform.smoothscale_by(frog, 0.4)

class Frog:
  def __init__(self):
    self.lives = 3
    self.y = 230
    self.velocity = 5
    self.mask = pygame.mask.from_surface(frog)

  def update(self):
    self.y += self.velocity
    self.velocity += 0.5
    if self.y > 230:
      self.y = 230
      self.velocity = - self.velocity/2                       
    if self.y < 0:
      self.y = 0
      self.velocity = 0

  def draw(self, screen):
    screen.blit(frog, (40,self.y))

    # self.mask.to_surface(screen, dest = (40, self.y))
