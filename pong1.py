import turtle
import os

wn = turtle.Screen()
wn.title("Pong por @diazdesandi")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350,0)

#Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350,0)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 2
pelota.dy = -2

#Funciones Paleta A
def paleta_a_arriba():
    y=paleta_a.ycor()
    y += 20
    paleta_a.sety(y)

def paleta_a_abajo():
    y=paleta_a.ycor()
    y -= 20
    paleta_a.sety(y)

#Funciones Paleta B
def paleta_b_arriba():
    y=paleta_b.ycor()
    y += 20
    paleta_b.sety(y)

def paleta_b_abajo():
    y=paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)

# Lectura de las teclas presionadas
wn.listen() #Lee el teclado
wn.onkeypress(paleta_a_arriba,"w") #Al pulsar tecla w, manda llamar funcion.
wn.onkeypress(paleta_a_abajo,"s")
wn.onkeypress(paleta_b_arriba, "Up")
wn.onkeypress(paleta_b_abajo,"Down")

#Ciclo principal del juego
while True:
    wn.update()

    # Movimiento de pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Delimitación del campo
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
    
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1