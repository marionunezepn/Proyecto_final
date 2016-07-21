import turtle
import os 
import math
import random
import pygame
#creacion de la pantalla de juego
pygame.init()#inicializacion de los modulos de ygame
sonido1 = pygame.mixer.Sound("shoot.wav")
sonido2 = pygame.mixer.Sound("son1.wav")
sonido3 = pygame.mixer.Sound("music1.ogg")
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Juego")
ventana.bgpic("Stars.gif")
#registro de imagenes
turtle.register_shape("image3.gif")
turtle.register_shape("image2.gif")
turtle.register_shape("image1.gif")
turtle.register_shape("bullet.gif")
#dibujo del borde 
borde = turtle.Turtle()
borde.speed(0)
borde.color("white")
borde.penup()
borde.setposition(-300,-300)
borde.pendown()
borde.pensize(3)
for side in range(5):
	borde.fd(650)
	borde.lt(90)
borde.hideturtle()
#puntaje
marcador = 0
#dibujo del puntaje
puntaje = turtle.Turtle()
puntaje.speed(0)
puntaje.color("white")
puntaje.penup()
puntaje.setposition(-290,280)
puntajestring = "Puntaje: %s" %marcador
puntaje.write(puntajestring,False,align = "left", font= ("Arial",14,"normal"))
puntaje.hideturtle()
#creacion del jugador con turtle
jugador = turtle.Turtle()
jugador.color("blue")
jugador.shape("image2.gif")
jugador.penup()
jugador.speed(0)
jugador.setposition(0,-250)
jugador.setheading(90)

velocidad_jugador = 15

#numero de enemigos
numero_de_enemigos = 5
#creacion de lista de enemigos
enemigos = []
#añaden a la lista los enemigos
for i in range (numero_de_enemigos):
	#creacion de enemigos
	enemigos.append(turtle.Turtle())

for enemigo in enemigos:
	enemigo.color("red")
	enemigo.shape("image1.gif")
	enemigo.penup()
	enemigo.speed(0)
	x= random.randint(-200,200)
	y = random.randint(100,250)
	enemigo.setposition(x,y)
enemigo_velocidad = 5

#creacion del disparo
disparo = turtle.Turtle()
disparo.color("yellow")
disparo.shape("bullet.gif")
disparo.penup()
disparo.speed(0)
disparo.setheading(90)
disparo.shapesize(0.5 , 0.5)
disparo.hideturtle()
velocidad_disparo = 20
#estado del disparo
estado_disparo = "listo" 

#creacion del disparo2
disparo2 = turtle.Turtle()
disparo2.color("yellow")
disparo2.shape("image3.gif")
disparo2.penup()
disparo2.speed(0)
disparo2.setheading(90)
disparo2.shapesize(0.5 , 0.5)
disparo2.hideturtle()
velocidad_disparo2 = 30
#estado del disparo
estado_disparo2 = "listo"

#movimiento de jugador de izquierda a derecha
def mover_izquierda():
	x= jugador.xcor()
	x -= velocidad_jugador
	if x<-280:
		x=-260
	jugador.setx(x)

def mover_derecha():
	x= jugador.xcor()
	x += velocidad_jugador
	if x>280:
		x=280
	jugador.setx(x)
def disparo_1():
	sonido1.play()
	global estado_disparo
	if estado_disparo == "listo":
		estado_disparo = "fuego"
		#movimiento dela bala con el jugador
		x = jugador.xcor()
		y = jugador.ycor() + 10
		disparo.setposition(x,y)
		disparo.showturtle()

def disparo_2():
	#sonido1.play()
	global estado_disparo2
	if estado_disparo2 == "listo":
		estado_disparo2 = "fuego"
		#movimiento dela bala con el jugador
		x = enemigo.xcor()
		y = enemigo.ycor() + 10
		disparo2.setposition(x,y)
		disparo2.showturtle()
def colision (t1,t2):
	distancia = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distancia < 30:
		return True
	else: 
		return False

#creacion de los eventos con el teclado
turtle.listen()
turtle.onkey(mover_izquierda,"Left")
turtle.onkey(mover_derecha,"Right")
turtle.onkey(disparo_1,"space")
Salir = True
alazar=0
sonido3.play()
while Salir==True:
	alazar +=1

	for enemigo in enemigos : 
		#movimiento de enemigo
		x = enemigo.xcor()
		x += enemigo_velocidad
		enemigo.setx(x)
		#movimiento del enemigo
		if enemigo.xcor() > 280:
			y = enemigo.ycor()
			y-= 40
			enemigo_velocidad *= -1

		if enemigo.xcor() < -260:
			y= enemigo.ycor()
			y-= 40
			enemigo_velocidad *= -1
			enemigo.sety(y)
		#disparo alazar
		if alazar%10==0:
			disparo_2()
			estado_disparo2="fuego"
			if estado_disparo2 == "fuego":
				y = disparo2.ycor()
				y -= velocidad_disparo2
				disparo2.sety(y)
	
			#chequeo de la bala hacia el tope
			if disparo2.ycor() <-300 :
				disparo2.hideturtle()
				estado_disparo2 = "listo"
			#chequeo de colision
			if colision(disparo2,jugador):
				Salir=False
				sonido2.play()
				puntajestring = "GAME OVER"
				puntaje.clear()
				puntaje.write(puntajestring,False,align = "left", font= ("Arial",14,"normal"))

		#chequeo de colision
		if colision(disparo,enemigo):
			sonido2.play()
			#reseteo del disparo
			disparo.hideturtle()
			estado_disparo = "listo"
			disparo.setposition(0,-400)
			#reseteo del enemigo
			x= random.randint(-200,200)
			y = random.randint(100,250)
			enemigo.setposition(x,y)
			marcador +=10
			puntajestring = "Puntaje: %s" %marcador
			puntaje.clear()
			puntaje.write(puntajestring,False,align = "left", font= ("Arial",14,"normal"))

		if colision(jugador, enemigo):
			sonido1.play()
			jugador.hideturtle()
			enemigo.hideturtle()
			puntajestring = "GAME OVER "
			puntaje.clear()
			puntaje.write(puntajestring,False,align = "left", font= ("Arial",14,"normal"))
			Salir=False

	#movimiento del disparo

	if estado_disparo == "fuego":
		y = disparo.ycor()
		y += velocidad_disparo
		disparo.sety(y)
	
	#chequeo de la bala hacia el tope
	if disparo.ycor() > 275 :
		disparo.hideturtle()
		estado_disparo = "listo"
	
	if marcador==100:
		Salir=False
		puntajestring = "VERY GOO, GOOD JOB "
		puntaje.clear()
		puntaje.write(puntajestring,False,align = "left", font= ("Arial",14,"normal"))






ventana.mainloop	()