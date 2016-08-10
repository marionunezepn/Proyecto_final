#declaracion de librerias
import pygame
from pygame.locals import *
from tkinter import *
from random import randint
from tkinter import *
#declaracion de variables locales
ancho = 700
alto = 600
ListaEnemigo=[] #variable que gurdara a los enemigos
# cambio de los botones al pasar el mouse
class Boton(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x=200,y=200):
		self.imagen_normal=imagen1 #imagen normal
		self.imagen_seleccion=imagen2 #imagen de cambio
		self.imagen_actual=self.imagen_normal 
		self.rect=self.imagen_actual.get_rect() #posicion
		self.rect.left,self.rect.top=(x,y)
	def update(self,pantalla,cursor): #cambia de imagen del boton cuando el mouse pasa por encima
		if cursor.colliderect(self.rect): #si colisiona 
			self.imagen_actual=self.imagen_seleccion #cambia
		else:
			self.imagen_actual=self.imagen_normal
		pantalla.blit(self.imagen_actual,self.rect)#si no se mantiene
#Mouse en la pantalla recoge la posicion
class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()
#crea una pantalla que muestra los controles de juego
def controles():
	salir = False
	pygame.init()
	screen = pygame.display.set_mode((400, 390))
	pygame.display.set_caption("Controles")
	ImagenFondo = pygame.image.load("Fondos/control.gif")
	botonModel1=pygame.image.load("Botones/btn1.gif")
	botonModel2=pygame.image.load("Botones/btn5.gif")
	boton1=Boton(botonModel1,botonModel2,50,320) #llama a la clase boton
	cursor1=Cursor() #activa el curso del mouse en la pantalla
	while salir!=True: #loop principal
		for event in pygame.event.get(): #recoore los eventos
			if event.type == QUIT: #cuando se cierra la pantalla
				salir = True
			if event.type==pygame.MOUSEBUTTONDOWN: #accion con el teclado
				if cursor1.colliderect(boton1.rect): #colision con el boton
					menuJuego()
					salir=True
		screen.blit(ImagenFondo,(0,0)) #pone el fondo de pantalla
		cursor1.update() #actualiza el boton
		boton1.update(screen,cursor1)#dibuja el boton en la pantalla
		pygame.display.update()
#creacion y grbacion en el txt
def creartxt():
	archi=open('Puntajes.txt','w')
	archi.close()
def grabartxt(l): #guarda los datos en el archivo
	archi=open('Puntajes.txt','a')
	archi.write(l+"\n")
	archi.close()
#muestra el contenido de un txt en pantalla(con listbox)
def puntajes():

	root = Tk()
	root.title('SCORES')
	archi=open('Puntajes.txt','r')
	linea=archi.read()
	li = linea.split("\n")
	listb = Listbox(root,width=40, height=10)
	for item in li:
		listb.insert(len(li),item)
	listb.pack()
	root.geometry('300x210+450+70')
	root.mainloop()
	"""linea=archi.readline()
	while linea!="":
		print (linea)
		linea=archi.readline()
	archi.close()"""

	"""linea=archi.read()
	cadena = linea
	var = ''
	for h in cadena:
		if cadena[h]=="":
			var ="Puntaje "+h+": " + var
			print(var)"""
#programacion para salir del programa
def salirJuego():
    import sys
    sys.exit(0)
#dibujo de la nave espacial
class naveEspacial(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("Fondos/image2.gif")
		self.ImagenExploscion = pygame.image.load("Fondos/explosion.gif")
		self.rect = self.ImagenNave.get_rect()
		#poscicion de la imgane en la pantalla de juego
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30
		#disparos del jugador
		self.ListaDisparo = []
		self.vida= True
		self.velocidad= 20
		#sonido
		self.sonido2 = pygame.mixer.Sound("Sonidos/shoot.wav")
		self.sonido3 = pygame.mixer.Sound("Sonidos/explosion.wav")
	#movimiento de la nave controlando los extremos
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
	#disparo del jugador y le agrega a la lista de disparo
	def dispara(self,x,y):
		MiProyectil  = proyectil(x,y,"Balas/image3.gif",True)
		self.ListaDisparo.append(MiProyectil)
		self.sonido2.play()
	#dibuja el jugador en la pantalla de juego
	def dibujar(self,superficie):
		superficie.blit(self.ImagenNave,self.rect)
	#cambia de imagen cuando colisiona con la nave enemiga
	def cambiar(self):
		self.sonido3.play()
		self.ImagenNave=self.ImagenExploscion
#dibujo del bala
class proyectil(pygame.sprite.Sprite):
	def __init__(self,posx,posy,ruta,personaje):
		pygame.sprite.Sprite.__init__(self)
		self.imageProyectil = pygame.image.load(ruta)
		self.rect=self.imageProyectil.get_rect()
		self.velocidadDisparo=5
		self.rect.top=posy
		self.rect.left=posx
		self.disparoPersonaje=personaje
	#movimiento de la vida dependiendo de quien dispare
	def trayectoria(self):
		if self.disparoPersonaje==False:
			self.rect.top=self.rect.top + self.velocidadDisparo
		else:
			self.rect.top=self.rect.top - self.velocidadDisparo	
	#dibuja la bala en la pantalla de juego	
	def dibujar(self,superficie):
		superficie.blit(self.imageProyectil, self.rect)
#Clase enemigos
class EnemigoI(pygame.sprite.Sprite):
	def __init__(self,posx,posy,distancia,imagen1):
		pygame.sprite.Sprite.__init__(self)
		self.imageA = pygame.image.load(imagen1) #carga la imagen
		self.rect=self.imageA.get_rect() #posicion a la imagen
		
		self.ListaDisparo=[]
		self.velocidad=20 #velocidad para el enemigo
		self.rect.top=posy #posciciones
		self.rect.left=posx
		self.rangoDisparo=5 # numero de disparos que puede dispara el enemigo
		self.derecha=True
		self.contador=0
		#controla movimiento en la pantalla de juego
		self.maxdescenso=self.rect.top+40
		self.limiteDerecha=posx + distancia
		self.limiteIzquierda=posx - distancia
		self.activar=True #para ver si la nave se sigue moviendo o no

	def comportamiento(self): #actividad que realiza el enemigo
		if self.activar==True:
			self.__movimientos()
			self.__ataque()
	def __movimientos(self):#movimiento en un pequeño rango de tiempo
		if self.contador<3:
			self.__movimientoLateral()
		else:
			self.__descenso()
	def __descenso(self):
		if self.maxdescenso>600: #sis se va de la pantalla se borra y se vuelve a crear
			self.maxdescenso=0
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
	#se mueve hasta el limite establecido en los lados
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


	def dibujar(self,superficie): # dibuja el enemigo en la pantalla
		self.ImagenInvasor=self.imageA
		superficie.blit(self.ImagenInvasor, self.rect)
	def __ataque(self):

		#controla el numero de balas que disparara el enemigo
		if (randint(0,100)<self.rangoDisparo):
			self.__disparo()

	def __disparo(self): #dibuja los disparos
		x,y = self.rect.center
		MiProyectil = proyectil(x,y,"Balas/bullet.gif",False)
		self.ListaDisparo.append(MiProyectil)
#creacion de enemigos
def cargarEnemigos(crearenemigos):
	for i in range(crearenemigos):
		enemigo=EnemigoI(randint(50,285),randint(-100,300),randint(50,300),"Movimiento/mov2.gif")
		ListaEnemigo.append(enemigo)
#carga los enemigos especiales
def cargarEnemigoEspecial(nivel):
	if nivel==1:
		enemigo=EnemigoI(270,-10,210,"Enemigos/enemigo1.gif")
		ListaEnemigo.append(enemigo)
	if nivel==2:
		enemigo=EnemigoI(270,-10,210,"Enemigos/enemigo2.gif")
		ListaEnemigo.append(enemigo)
	if nivel==3:
		enemigo=EnemigoI(270,-10,210,"Enemigos/enemigo3.gif")
		ListaEnemigo.append(enemigo)
#pantalla de juego
def PantallaJuego():
	pygame.init()
	pantalla = pygame.display.set_mode([700,600])
	salir = False
	pygame.display.set_caption(" juego")
	ImagenFondo = pygame.image.load("Fondos/Stars.gif")
	sonido1 = pygame.mixer.Sound("Sonidos/music1.wav")	
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
	segundosint=0
	puntaje=0
	score = ""
	while salir != True:#Loop principal	
		try :

			reloj.tick(60)	
			score = fuente1.render("SCORE: "+str(puntaje),0,(255,255,255))
			for event in pygame.event.get(): #recoore todo los eventos
				if event.type == pygame.QUIT: #cuando se cierra la ventana
					salir = True
				if enJuego == True: # para que despues no pueda realizar ninguna actividad
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
							grabartxt(str(puntaje))
							menuJuego()
							salir=True

			pantalla.blit(ImagenFondo,(0,0))

			#niveles
			if Nivel==1: #impresion
				info = fuente1.render("LEVEL 1",0,(255,255,255))
				pantalla.blit(info,(350,300))
			if Nivel==1:
				if enJuego2 == False :
					#creacion de enemigos cuando ya elimino a todos
					if len(ListaEnemigo)==0 and crearenemigos<=2 and conE==True:
						crearenemigos+=1
						cargarEnemigos(crearenemigos)
						enJuego2=True
				#carga el enemigo especial cuando ya acabo con los enemigos principales
				if crearenemigos==3 and len(ListaEnemigo)==0 and conE==True:
					cargarEnemigoEspecial(Nivel)
					crearenemigos+=1
				#cuando ya elimina al enemigo especial
				if crearenemigos==4 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==5:
					enJuego=False
					enemigo.activar=False
					#borra todo (disparos de enemigo y jugador y la lista de enemigos)
					#reinicia todos los valores
					for enemigo in ListaEnemigo:
						ListaEnemigo.remove(enemigo)
					Nivel=2
					crearenemigos=0
					enJuego=True
					enemigo.activar=True
					enemigoVida=1
					conE=True
			else:
				info = fuente1.render("GAME OVER",0,(255,255,255))
					
			if Nivel==2:#impresion
				info = fuente1.render("LEVEL 2",0,(255,255,255))
				pantalla.blit(info,(350,300))

			if Nivel==2:
				if enJuego2 == False :
					#creacion de enemigos cuando ya elimino a todos
					if len(ListaEnemigo)==0 and crearenemigos<=3 and conE==True:
						crearenemigos+=1
						cargarEnemigos(crearenemigos)
						enJuego2=True
				#carga el enemigo especial cuando ya acabo con los enemigos principales
				if crearenemigos==4 and len(ListaEnemigo)==0 and conE==True:
					cargarEnemigoEspecial(Nivel)
					crearenemigos+=1
				#cuando ya elimina al enemigo especial
				if crearenemigos==5 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==8:
					enJuego=False
					enemigo.activar=False
					#borra todo (disparos de enemigo y jugador y la lista de enemigos)
					#reinicia todos los valores
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
				pantalla.blit(info,(350,300))

			if Nivel==3:#impresion
				info = fuente1.render("GAME OVER",0,(255,255,255))
				if enJuego2 == False :
					#creacion de enemigos cuando ya elimino a todos
					if len(ListaEnemigo)==0 and crearenemigos<=4 and conE==True:
						crearenemigos+=1
						cargarEnemigos(crearenemigos)
						enJuego2=True
				#carga el enemigo especial cuando ya acabo con los enemigos principales		
				if crearenemigos==5 and len(ListaEnemigo)==0 and conE==True:
					cargarEnemigoEspecial(Nivel)
					crearenemigos+=1
				#cuando ya elimina al enemigo especial
				if crearenemigos==6 and len(ListaEnemigo)!=0 and conE==True and enemigoVida==11:
					enJuego=False
					enemigo.activar=False
					for enemigo in ListaEnemigo:
						ListaEnemigo.remove(enemigo)
					
					Nivel=4	
			if Nivel==4:
				info = fuente1.render("COMPLETED GAME!!",0,(255,255,255))
				sonido1.stop()

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
										puntaje+=10	
										ListaEnemigo.remove(enemigo)
										#print("vidaenemigo:"+str(enemigoVida))
										cargarEnemigoEspecial(Nivel)
									else:
										ListaEnemigo.remove(enemigo)
										enJuego2=False
										puntaje+=10	
										score = fuente1.render("SCORE: "+str(puntaje),0,(255,255,255))
										
								if Nivel==2:						
									if crearenemigos==5 and len(ListaEnemigo)!=0 and conE==True:
										enemigoVida+=1
										puntaje+=10	
										ListaEnemigo.remove(enemigo)
										#print("vidaenemigo:"+str(enemigoVida))
										cargarEnemigoEspecial(Nivel)
									else:
										ListaEnemigo.remove(enemigo)
										enJuego2=False
										puntaje+=10	
										print(puntaje)
								if Nivel==3:						
									if crearenemigos==6 and len(ListaEnemigo)!=0 and conE==True:
										enemigoVida+=1
										puntaje+=10	
										ListaEnemigo.remove(enemigo)
										#print("vidaenemigo:"+str(enemigoVida))
										cargarEnemigoEspecial(Nivel)
									else:
										ListaEnemigo.remove(enemigo)
										enJuego2=False
										puntaje+=10	
										print(puntaje)
								
			pantalla.blit(score,(50,550))
			#choque de enemigo con el jugador
			if len(ListaEnemigo)>0:
				for enemigo in ListaEnemigo:
					enemigo.comportamiento()
					enemigo.dibujar(pantalla)
					if enemigo.rect.colliderect(jugador.rect):
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
						if x.rect.top >700:
							enemigo.ListaDisparo.remove(x)
						else:
							#bala contra bala
							for disparo in jugador.ListaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.ListaDisparo.remove(disparo)
									enemigo.ListaDisparo.remove(x)
			if enJuego==True:
				segundosint = pygame.time.get_ticks()/1000
				segundos = str(segundosint)
				contador1 = fuente1.render("TIME: "+segundos,0,(255,255,255))
				pantalla.blit(contador1,(550,550))
			

			if enJuego==False or conE==False:
				pantalla.blit(info,(330,330))
				pantalla.blit(contador1,(450,30))
				pantalla.blit(score,(450,80))
				

									
			pygame.display.update()
		except ValueError:
			print("Oops! No era válido. Intente nuevamente...")
#menu de juego
def menuJuego():
	salir = False
	pygame.init()
	screen = pygame.display.set_mode((400, 380))
	pygame.display.set_caption("MENU")
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
	while salir !=True:
		for event in pygame.event.get():
			if event.type == QUIT:
				salir = True
			if event.type==pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(boton1.rect):
					PantallaJuego()
					salir=True
				if cursor1.colliderect(boton4.rect):
					salirJuego()
				if cursor1.colliderect(boton3.rect):
					puntajes()
				if cursor1.colliderect(boton2.rect):
					controles()

		screen.blit(ImagenFondo,(0,0))
		cursor1.update()
		boton1.update(screen,cursor1)
		boton2.update(screen,cursor1)
		boton3.update(screen,cursor1)
		boton4.update(screen,cursor1)
		pygame.display.update()
#llama a los metodos iniciales

creartxt()
menuJuego()
