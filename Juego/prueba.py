#importamos librerias
import pygame
from pygame.locals import *

#iniciamos pygame
pygame.init()

#definimos constantes
pantalla = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Titulo de ventana')

reloj = pygame.time.Clock()

#definimos clases
class Pelota(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.imagen = cargar_imagen("datos/pelota.png", True)
  self.rect = self.imagen.get_rect()
  self.rect.centerx = 640 / 2
  self.rect.centery = 480 / 2
  self.speed = [0.5, -0.5]
 def actualizar(self, time):
  self.rect.centerx += self.speed[0] * time
  self.rect.centery += self.speed[1] * time
  if self.rect.left <= 0 or self.rect.right >= 640:
   self.speed[0] = -self.speed[0]
   self.rect.centerx += self.speed[0] * time
  if self.rect.top <= 0 or self.rect.bottom >= 480:
   self.speed[1] = -self.speed[1]
   self.rect.centery += self.speed[1] * time



#definimos funciones
def cargar_imagen(nombre,transparente=False):
     imagen = pygame.image.load("images.jpg")
     imagen = imagen.convert()
     if transparente:
          color = imagen.get_at((0,0))
          imagen.set_colorkey(color, RLEACCEL)
     return imagen

fondo = cargar_imagen('fondo.png')
pelota = Pelota()

#Bucle principal del juego
while 1:
 time = reloj.tick(60)
 pelota.actualizar(time)
 for event in pygame.event.get():
  if event.type == QUIT:
   pygame.quit()
   sys.exit()
  elif event.type == KEYDOWN:
   if event.type == K_ESCAPE:
    pygame.quit()
    sys.exit()
 pantalla.blit(fondo, (0, 0)) 
 pantalla.blit(pelota.imagen, pelota.rect)
 pygame.display.flip()