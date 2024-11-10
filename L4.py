import pgzrun
import random

WIDTH = 500
HEIGHT = 500

x = 200
y = 50
p = 0
h = 0
t = 0

alien = Actor("alien")
title = "Click on the alien"
percentage = ""
def on_mouse_down(pos):
	global title, h, p, t

	if alien.collidepoint(pos):
		alien.x = random.randint(50,450)
		alien.y = random.randint(50,450)
		title = "You hit"
		t += 1
		h += 1
		p = (h/t)*100
	else:
		title = "You missed"
		t += 1
		p = (h/t)*100

def draw():
	screen.fill("blue")
	alien.draw()
	screen.draw.text(title,(x,y))
	screen.draw.text(percentage+str(p)+"%",(400,50))

pgzrun.go()