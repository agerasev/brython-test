from linalg import *

import utest


class Point2:
	def __init__(self, mass=1.0, pos=Float2(), vel=Float2()):
		self.mass = mass
		self.pos = pos
		self.vel = vel
		self.acc = Float2()

	def force(self, f):
		self.acc += f/self.mass

	def step(self, dt):
		self.vel += self.acc*dt
		self.pos += self.vel*dt
		self.acc = Float2()

class Point2RK4(Point2):
	def __init__(self, *args):
		super().__init__(*args)
		self._kvs = 4*[None]
		self._kps = 4*[None]
		self._vel = None
		self._pos = None

	def pre_step(self):
		self._vel = self.vel
		self._pos = self.pos

	def step(self, k, dt):
		self._kvs[k] = self.acc*dt
		self._kps[k] = self.vel*dt
		hf = 0.5 if k < 2 else 1.0
		self.vel = self._vel + self._kvs[k]*hf
		self.pos = self._pos + self._kps[k]*hf
		self.acc = Float2()

	def post_step(self, dt):
		self.pos = self._pos + (self._kps[0] + 2*self._kps[1] + 2*self._kps[2] + self._kps[3])/6.0
		self.vel = self._vel + (self._kvs[0] + 2*self._kvs[1] + 2*self._kvs[2] + self._kvs[3])/6.0
