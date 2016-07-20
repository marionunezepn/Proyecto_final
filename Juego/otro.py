import pygame
import random
class player(pygame.sprite.Sprite):
	def __init__(self,imagen):
		self.imagen=imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(100,200)
	def disparo(self,imagen):
		self.imagen=imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(player1.pos())

	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
	def update(self,superficie):
		superficie.blit(self.imagen,self.rect)
def main(): #menu principal
	pygame.init()#inicializacion de los modulos de ygame
	pantalla = pygame.display.set_mode([700,600]) #tamaño de la ventana
	pygame.display.set_caption("Juego")#nombre
	reloj1 = pygame.time.Clock()
	salir=False
	imagen1=pygame.image.load("image2.gif")
	imagen2=pygame.image.load("bullet.gif")
	
	
	imagenfondo = pygame.image.load("Stars.gif").convert_alpha()
	player1=player(imagen1)
	sprite1= pygame.sprite.Sprite()
	sprite1.image=imagen2
	sprite1.rect=imagen2.get_rect()
	sprite1.rect.top = player1.rect.top
	sprite1.rect.left = player1.rect.left
	vx,vy=0,0
	velocidad=10
	disparo=1;
	while salir != True:#Loop principal
		for event in pygame.event.get(): #recoore todo los eventos
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					vx=-velocidad
				if event.key == pygame.K_RIGHT:
					vx=velocidad
				if event.key == pygame.K_UP:
					vy=-velocidad
				if event.key == pygame.K_DOWN:
					vy=velocidad
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					vx=0
				if event.key == pygame.K_RIGHT:
					vx=0
				if event.key == pygame.K_UP:
					vy=0
				if event.key == pygame.K_DOWN:
					vy=0
				if event.key == pygame.K_SPACE:
					disparo=0

		reloj1.tick(20) 	
		player1.mover(vx,vy)
		pantalla.fill((0,0,0))#pintar de color blanco
		pantalla.blit(imagenfondo,(0,0))	
		#pantalla.blit(imagen2,(player1.pos())
		if(disparo==0):
			pantalla.blit(sprite1.image,(player1.rect.top,player1.rect.left))
			disparo=1
		player1.update(pantalla)
		pygame.display.update()
	
	pygame.quit()
main()