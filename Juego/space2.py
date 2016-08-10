import pygame
from pygame.locals import *
from tkinter import *
from random import randint
ancho = 700
alto = 600
ListaEnemigo=[]
class Boton(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x=200,y=200):
		self.imagen_normal=imagen1
		self.imagen_seleccion=imagen2
		self.imagen_actual=self.imagen_normal
		self.rect=self.imagen_actual.get_rect()
		self.rect.left,self.rect.top=(x,y)
	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.imagen_actual=self.imagen_seleccion
		else:
			self.imagen_actual=self.imagen_normal
		pantalla.blit(self.imagen_actual,self.rect)
class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()
def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")

def salirJuego():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)
class naveEspacial(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("image2.gif")
		self.ImagenExploscion = pygame.image.load("Fondos/explosion.gif")
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30
		self.ListaDisparo = []
		self.vida= True
		self.velocidad= 20
		self.sonido2 = pygame.mixer.Sound("shoot.wav")
		self.sonido3 = pygame.mixer.Sound("Sonidos/explosion.wav")
	def movimientoDerecha(self):
		self.rect.right+=self.velocidad
		self.__movimiento()
	def movimientoIzquierda(self):
		self.rect.left-=self.velocidad
		self.__movimiento()
	def __movimiento(self):
		if self.vida==True:
			if self.rect.left <=0:
				self.rect.left=0
			elif self.rect.right>700:
				self.rect.right=700
	def dispara(self,x,y):
		MiProyectil  = proyectil(x,y,"image3.gif",True)
		self.ListaDisparo.append(MiProyectil)
		self.sonido2.play()
	def dibujar(self,superficie):

		superficie.blit(self.ImagenNave,self.rect)
	def cambiar(self):
		self.sonido3.play()
		self.ImagenNave=self.ImagenExploscion

class proyectil(pygame.sprite.Sprite):
	def __init__(self,posx,posy,ruta,personaje):
		pygame.sprite.Sprite.__init__(self)
		self.imageProyectil = pygame.image.load(ruta)
		self.rect=self.imageProyectil.get_rect()
		self.velocidadDisparo=5
		self.rect.top=posy
		self.rect.left=posx
		self.disparoPersonaje=personaje

	def trayectoria(self):
		if self.disparoPersonaje==False:
			self.rect.top=self.rect.top + self.velocidadDisparo
		else:
			self.rect.top=self.rect.top - self.velocidadDisparo		
	def dibujar(self,superficie):
		superficie.blit(self.imageProyectil, self.rect)
class invasor(pygame.sprite.Sprite):
	def __init__(self,posx,posy,distancia,imagen1,imagen2):
		pygame.sprite.Sprite.__init__(self)
		self.imageA = pygame.image.load(imagen1)
		self.imageB = pygame.image.load(imagen2)

		self.listaImagenes=[self.imageA,self.imageB]
		self.posImagen=0

		self.ImagenInvasor=self.listaImagenes[self.posImagen]
		self.rect=self.ImagenInvasor.get_rect()
		
		self.ListaDisparo=[]
		self.velocidad=20
		self.rect.top=posy
		self.rect.left=posx

		self.rangoDisparo=5
		self.tiempoCambio=5

		self.derecha=True
		self.contador=0
		self.maxdescenso=self.rect.top+40

		self.limiteDerecha=posx + distancia
		self.limiteIzquierda=posx - distancia
		self.activar=True

	def comportamiento(self,tiempo):
		if self.activar==True:
			self.__movimientos()
			self.__ataque()
			if self.tiempoCambio==tiempo:
				self.posImagen+=1
				self.tiempoCambio+=1
				if self.posImagen > len(self.listaImagenes)-1:
					self.posImagen=0
	def __movimientos(self):
		if self.contador<3:
			self.__movimientoLateral()
		else:
			self.__descenso()
	def __descenso(self):
		if self.maxdescenso>600:
			self.maxdescenso=0
			#print(len(ListaEnemigo))
			crear=len(ListaEnemigo)
			for enemigo in ListaEnemigo:
				ListaEnemigo.remove(enemigo)
			cargarEnemigos(crear)
		else:
			if self.maxdescenso==self.rect.top:
				self.contador=0
				self.maxdescenso=self.rect.top+40
			else:
				self.rect.top+=1
	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left=self.rect.left+self.velocidad
			if self.rect.left > self.limiteDerecha:
				self.derecha=False
				self.contador+=1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < self.limiteIzquierda: 
				self.derecha =True


	def dibujar(self,superficie):
		self.ImagenInvasor=self.listaImagenes[self.posImagen]
		superficie.blit(self.ImagenInvasor, self.rect)
	def __ataque(self):
		if (randint(0,100)<self.rangoDisparo):
			self.__disparo()

	def __disparo(self):
		x,y = self.rect.center
		MiProyectil = proyectil(x,y,"bullet.gif",False)
		self.ListaDisparo.append(MiProyectil)
def cargarEnemigos(crearenemigos):
	for i in range(crearenemigos):
		enemigo=invasor(randint(50,285),randint(-100,300),randint(50,300),"Movimiento/mov2.gif","Movimiento/mov1.gif")
		ListaEnemigo.append(enemigo)
def cargarEnemigoEspecial(nivel):
	if nivel==1:
		enemigo=invasor(270,-10,210,"Enemigos/enemigo1.gif","Enemigos/enemigo1.gif")
		ListaEnemigo.append(enemigo)
	if nivel==2:
		enemigo=invasor(270,-10,210,"Enemigos/enemigo2.gif","Enemigos/enemigo2.gif")
		ListaEnemigo.append(enemigo)
	if nivel==3:
		enemigo=invasor(270,-10,210,"Enemigos/enemigo3.gif","Enemigos/enemigo3.gif")
		ListaEnemigo.append(enemigo)
def PantallaJuego():
	pygame.init()
	pantalla = pygame.display.set_mode([700,600])
	salir = False
	pygame.display.set_caption(" juego")
	ImagenFondo = pygame.image.load("Stars.gif")
	sonido1 = pygame.mixer.Sound("music1.wav")	
	sonido1.play()
	fuente1 = pygame.font.SysFont("Arial",24,True,False	)
	info = fuente1.render("",0,(255,255,255))
	jugador = naveEspacial()
	enJuego=True
	enJuego2=True
	conE=True
	reloj = pygame.time.Clock()
	crearenemigos=1
	enemigoespecial=0
	enemigoVida=0
	Nivel=1
	cargarEnemigos(crearenemigos)
	tiempo=0
	while salir != True:#Loop principal		
		reloj.tick(60)
		for event in pygame.event.get(): #recoore todo los eventos
			if event.type == pygame.QUIT: #cuando se cierra la ventana
				salir = True

			if enJuego == True:
				if event.type == pygame.KEYDOWN: # movimeinto con el teclado
					if event.key == pygame.K_LEFT:
						jugador.movimientoIzquierda()
					if event.key == pygame.K_RIGHT:
						jugador.movimientoDerecha()
					if event.key == pygame.K_SPACE:
						x,y=jugador.rect.center
						jugador.dispara(x,y)
			if enJuego == False:
				sonido1.stop()
				if event.type == pygame.KEYDOWN:
					if event.key ==pygame.K_c:
						menuJuego()
						salir=True

		pantalla.blit(ImagenFondo,(0,0))

		#niveles

		#carga enemigos
		if Nivel==1:
			info = fuente1.render("LEVEL 1",0,(255,255,255))
			pantalla.blit(info,(350,300))
		if Nivel==1:

			if enJuego2 == False :
					if len(ListaEnemigo)==0 and crearenemigos<=2 and conE==True:
						crearenemigos+=1
						#print(crearenemigos)
						cargarEnemigos(crearenemigos)
						enJuego2=True

			if crearenemigos==3 and len(ListaEnemigo)==0 and conE==True:
				cargarEnemigoEspecial(Nivel)
				crearenemigos+=1
			if crearenemigos==4 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==5:
				enJuego=False
				enemigo.activar=False
				for enemigo in ListaEnemigo:
					ListaEnemigo.remove(enemigo)
				#info = fuente1.render("Nivel superado preciona C para continuar",0,(255,255,255))
				Nivel=2
				crearenemigos=0
				enJuego=True
				enemigo.activar=True
				enemigoVida=1
				conE=True
		else:
			info = fuente1.render("GAME OVER",0,(255,255,255))
				
		if Nivel==2:
			info = fuente1.render("LEVEL 2",0,(255,255,255))
			pantalla.blit(info,(350,300))

		if Nivel==2:
			#enJuego2=True
			if enJuego2 == False :
					if len(ListaEnemigo)==0 and crearenemigos<=3 and conE==True:
						crearenemigos+=1
						#print(crearenemigos)
						cargarEnemigos(crearenemigos)
						enJuego2=True

			if crearenemigos==4 and len(ListaEnemigo)==0 and conE==True:
				cargarEnemigoEspecial(Nivel)
				crearenemigos+=1
			if crearenemigos==5 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==5:
				enJuego=False
				enemigo.activar=False
				for enemigo in ListaEnemigo:
					ListaEnemigo.remove(enemigo)
				Nivel=3
				crearenemigos=0
				enJuego=True
				enemigo.activar=True
				enemigoVida=1
				conE=True
		else:
			info = fuente1.render("GAME OVER",0,(255,255,255))
		if Nivel==3:
			info = fuente1.render("LEVEL 3",0,(255,255,255))
			pantalla.blit(info,(200,300))

		if Nivel==3:
			#enJuego2=True
			if enJuego2 == False :
					if len(ListaEnemigo)==0 and crearenemigos<=4 and conE==True:
						crearenemigos+=1
						#print(crearenemigos)
						cargarEnemigos(crearenemigos)
						enJuego2=True

			if crearenemigos==5 and len(ListaEnemigo)==0 and conE==True:
				cargarEnemigoEspecial(Nivel)
				crearenemigos+=1
			if crearenemigos==6 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==5:
				enJuego=False
				enemigo.activar=False
				for enemigo in ListaEnemigo:
					ListaEnemigo.remove(enemigo)
				info = fuente1.render("JUEGO COMPLETADO",0,(255,255,255))
				Nivel=4	
		else:
			info = fuente1.render("GAME OVER",0,(255,255,255))

		

		tiempo+=1
		jugador.dibujar(pantalla)
		#bala de jugador contra enemigo
		if len (jugador.ListaDisparo)>0:
			for x in jugador.ListaDisparo:
				x.dibujar(pantalla)
				x.trayectoria()
				if x.rect.top<10:
					jugador.ListaDisparo.remove(x)
				else:
					for enemigo in ListaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							
							jugador.ListaDisparo.remove(x)
							if Nivel==1:						
								if crearenemigos==4 and len(ListaEnemigo)!=0 and conE==True:
									enemigoVida+=1
									ListaEnemigo.remove(enemigo)
									print("vidaenemigo:"+str(enemigoVida))
									cargarEnemigoEspecial(Nivel)
									#if enemigoVida==10:
									#	ListaEnemigo.remove(enemigo)
								else:
									ListaEnemigo.remove(enemigo)
									enJuego2=False	
							if Nivel==2:						
								if crearenemigos==5 and len(ListaEnemigo)!=0 and conE==True:
									enemigoVida+=1
									ListaEnemigo.remove(enemigo)
									print("vidaenemigo:"+str(enemigoVida))
									cargarEnemigoEspecial(Nivel)
									#if enemigoVida==10:
									#	ListaEnemigo.remove(enemigo)
								else:
									ListaEnemigo.remove(enemigo)
									enJuego2=False
							if Nivel==3:						
								if crearenemigos==6 and len(ListaEnemigo)!=0 and conE==True:
									enemigoVida+=1
									ListaEnemigo.remove(enemigo)
									print("vidaenemigo:"+str(enemigoVida))
									cargarEnemigoEspecial(Nivel)
									#if enemigoVida==10:
									#	ListaEnemigo.remove(enemigo)
								else:
									ListaEnemigo.remove(enemigo)
									enJuego2=False
							
		#choque de enemigo con el jugador
		if len(ListaEnemigo)>0:
			for enemigo in ListaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(pantalla)
				if enemigo.rect.colliderect(jugador.rect):
					sys.exit(0)
					sonido1.stop()
		
			if len (enemigo.ListaDisparo)>0:
				for x in enemigo.ListaDisparo:
					x.dibujar(pantalla)
					x.trayectoria()
					if x.rect.colliderect(jugador.rect):
						#bala de enemigo contra el jugador
						jugador.cambiar()
						for enemigo in ListaEnemigo:
							enemigo.activar=False
						for enemigo in ListaEnemigo:
							ListaEnemigo.remove(enemigo)
						for disparo in jugador.ListaDisparo:
							jugador.ListaDisparo.remove(disparo)
						for disparo in enemigo.ListaDisparo:
							enemigo.ListaDisparo.remove(disparo)
						enJuego=False
						conE=False
						sonido1.stop()
						#reloj.tick(60)
						
						
					if x.rect.top >700:
						enemigo.ListaDisparo.remove(x)
					else:
						#bala contra bala
						for disparo in jugador.ListaDisparo:
							if x.rect.colliderect(disparo.rect):
								jugador.ListaDisparo.remove(disparo)
								enemigo.ListaDisparo.remove(x)
		if enJuego==False or conE==False:
			pantalla.blit(info,(330,330))

								
		pygame.display.update()

def menuJuego():
	salir = False
	pygame.init()
	screen = pygame.display.set_mode((400, 380))
	pygame.display.set_caption("MENU")
	reloj1=pygame.time.Clock()
	ImagenFondo = pygame.image.load("Fondos/image.gif")
	botonModel1=pygame.image.load("Botones/btn1.gif")
	botonModel2=pygame.image.load("Botones/btn1.1.gif")
	botonModel3=pygame.image.load("Botones/btn4.gif")
	botonModel4=pygame.image.load("Botones/btn3.gif")
	botonModel5=pygame.image.load("Botones/btn2.gif")
	boton1=Boton(botonModel1,botonModel2,50,20)
	boton2=Boton(botonModel1,botonModel3,50,100)
	boton3=Boton(botonModel1,botonModel4,50,180)
	boton4=Boton(botonModel1,botonModel5,50,260)
	cursor1=Cursor()
	blanco=(0,0,0)
	while not salir:

		for e in pygame.event.get():
			if e.type == QUIT:
				salir = True
			if e.type==pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(boton1.rect):
					PantallaJuego()
					salir=True
				if cursor1.colliderect(boton4.rect):
					salirJuego()

		reloj1.tick(20)
		#screen.fill(ImagenFondo,0,0)
		screen.blit(ImagenFondo,(0,0))
		cursor1.update()
		boton1.update(screen,cursor1)
		boton2.update(screen,cursor1)
		boton3.update(screen,cursor1)
		boton4.update(screen,cursor1)
		pygame.display.update()

menuJuego()
