import pygame
import random
def main(): #menu principal
	pygame.init()#inicializacion de los modulos de ygame
	pantalla = pygame.display.set_mode([700,600]) #tamaño de la ventana
	pygame.display.set_caption(" juego")#nombre
	salir = False
	reloj1 = pygame.time.Clock()
	#colores
	blanco = (255,255,255)#color blanco
	rojizo = (200,20,50)
	azulado = (70,70,190)
	#superficies
	s1 = pygame.Surface((100,150))
	s2 = pygame.Surface((25,25))
	#rectangulo
	r1 = pygame.Rect(0,0,25,25)
	r2 = pygame.Rect (100,100,50,50)
	#poner color a las superficies
	s1.fill(rojizo)
	s2.fill(azulado)
	listarec=[]
	for x in range (15):
		w = random.randrange(10,30)
		h = random.randrange(20,40)
		x = random.randrange(450)
		y = random.randrange(450)
		listarec.append(pygame.Rect(x,y,w,h))
	while salir != True:#Loop principal
		for event in pygame.event.get(): #recoore todo los eventos
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				for recs in listarec:
					if r1.colliderect(recs):
						recs.width=0
						recs.height=0
			#movimiento con el mouse
			#(xant,yant) = (r1.left,r1.top)
			#(r1.left,r1.top)=pygame.mouse.get_pos()
			#r1.left -= r1.width/2
			#r1.top -= r1.height/2
			#if r1.colliderect(r2):
				#(r1.left,r1.top) = (xant,yant)
			#movimiento con el teclado
			#if event.type == pygame.KEYDOWN:
			#	if event.key == pygame.K_LEFT:
			#		r1.move_ip(-10,0)
			#	if event.key == pygame.K_RIGHT:
			#		r1.move_ip(10,0)
			#	if event.key == pygame.K_UP:
			#		r1.move_ip(0,-10)
			#	if event.key == pygame.K_DOWN:
			#		r1.move_ip(0,10)
					

			#if event.type == pygame.MOUSEBUTTONDOWN:
				#r1 = r1.move(10,10)
				#r1.move_ip(10,10)
			#if event.type == pygame.MOUSEMOTION:
				#r1 = r1.move(-10,-10)
		reloj1.tick(20) # limita 20 frames por segundo
		(r1.left,r1.top)=pygame.mouse.get_pos()
		pantalla.fill((0,0,0))#pintar de color blanco
		#pantalla.blit(s2,(10,10))
		#pantalla.blit(s1,(100,200))#superfice en el fondo
		#pygame.draw.rect(pantalla,rojizo,r1)
		#pygame.draw.rect(pantalla,azulado,r2)
		#dibujo de rectangulo
		for recs in listarec:
			pygame.draw.rect(pantalla,(0,200,20),recs)
		pygame.draw.rect(pantalla,rojizo,r1)
		pygame.display.update()
	
	pygame.quit()
main()