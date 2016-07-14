import pygame
import random
def main(): #menu principal
	pygame.init()#inicializacion de los modulos de ygame
	pantalla = pygame.display.set_mode([700,600]) #tamaño de la ventana
	imagen1 = pygame.image.load("images.jpg")
	(x,y)=(100,100)
	vx=0;
	r1 = pygame.Rect(350,50,25,500)
	sprite1= pygame.sprite.Sprite()
	sprite1.image=imagen1
	sprite1.rect=imagen1.get_rect()
	sprite1.rect.top = 50
	sprite1.rect.left = 50
	pygame.display.set_caption("Imagenes")#nombre
	reloj1 = pygame.time.Clock()
	salir=False
	while salir != True:#Loop principal
		for event in pygame.event.get(): #recoore todo los eventos
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					vx-=10
				
				if event.key == pygame.K_RIGHT:
					vx+=10
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					vx=0
				if event.key == pygame.K_RIGHT:
					vx=0
				#if event.key == pygame.K_UP:

					
				#if event.key == pygame.K_DOWN:
		oldx=sprite1.rect.left
		sprite1.rect.move_ip(vx,0)
		if sprite1.rect.colliderect(r1):
			sprite1.rect.left=oldx
		#x+=vx			
		reloj1.tick(20) 	
		pantalla.fill((0,0,0))#pintar de color blanc0
		#pantalla.blit(imagen1,(x,y))
		pygame.draw.rect(pantalla,(0,255,0),r1)	
		pantalla.blit(sprite1.image,sprite1.rect)
		pygame.display.update()
	
	pygame.quit()
main()