import math

from linalg import *
from physics import *

import browser
from browser import timer

cnv = browser.document["canvas"]
ctx = cnv.getContext("2d")

bodies = [
	Point2RK4(10, Float2(200, 300), Float2(0,-100)),
	Point2RK4(10, Float2(600, 300), Float2(0, 100))
]

G = 4.0e6

def gravity(bodies):
	for i, b0 in enumerate(bodies):
		for b1 in bodies[i+1:]:
			r = b1.pos - b0.pos
			f = (r*G)/(abs(r)**3)
			b0.acc += b1.mass*f
			b1.acc -= b0.mass*f

def step(dt, acc_fn):
	acc_fn(bodies)
	for b in bodies:
		b.step(dt)

def step_rk4(dt, acc_fn):
	for b in bodies:
		b.pre_step()
	for k in range(4):
		acc_fn(bodies)
		for b in bodies:
			b.step(k,dt)
	for b in bodies:
		b.post_step(dt)

def run(dt):
	step_rk4(dt, gravity)

	ctx.fillStyle = "rgba(0,0,0,0.01)"
	ctx.fillRect(0,0,cnv.width, cnv.height)

	ctx.fillStyle = "#FFFFFF"
	for b in bodies:
		ctx.beginPath()
		ctx.arc(b.pos.x, b.pos.y, b.mass, 0, 2*math.pi)
		ctx.fill()

	timer.set_timeout(lambda: run(dt), 1000*dt)

run(0.02)

print("main.py loaded")
