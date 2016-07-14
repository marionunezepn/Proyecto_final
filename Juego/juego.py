import pygame
import random
def main(): #menu principal
	pygame.init()#inicializacion de los modulos de ygame
	sonido1 = pygame.mixer.Sound("son1.wav")
	pantalla = pygame.display.set_mode([700,600]) #tamaño de la ventana
	pygame.display.set_caption(" juego")#nombre
	salir = False
	termino = False
	rotos = 0
	reloj1 = pygame.time.Clock()
	fuente1 = pygame.font.SysFont("Arial",24,True,False	)
	info = fuente1.render("Tienes 10 segundo para romper los rectangulos",0,(255,255,255))
	#fuente1 = pygame.font.Font(None,48)
	#texto1= fuente1.render("JUEGO DE RECTANGULOS",0,(255,230,245))
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
	segundosint=0
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
				if termino == False:
					for recs in listarec:
						if r1.colliderect(recs):
							sonido1.play()
							recs.width=0
							recs.height=0
							rotos +=1
			
		reloj1.tick(20) # limita 20 frames por segundo
		(r1.left,r1.top)=pygame.mouse.get_pos()
		pantalla.fill((0,0,0))#pintar de color blanco
		pantalla.blit(info,(150,200))
		if segundosint>=10:
			termino = True
		if termino==False:
			segundosint = pygame.time.get_ticks()/1000
			segundos = str(segundosint)
			contador1 = fuente1.render(segundos,0,(0,0,230))
		else:
			contador1 = fuente1.render(segundos+" Usted rompio:"+str(rotos),0,(0,0,230))

		pantalla.blit(contador1,(300,5))
		for recs in listarec:
			pygame.draw.rect(pantalla,(0,200,20),recs)
		pygame.draw.rect(pantalla,rojizo,r1)
		pygame.display.update()
	
	pygame.quit()
main()