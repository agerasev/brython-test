import math

import utest


class Float2:
	def __init__(self, *args):
		if len(args) == 0:
			self.x, self.y = 0.0, 0.0
		elif len(args) == 1:
			if isinstance(args[0], Float2):
				self.x, self.y = float(args[0].x), float(args[0].y)
			else:
				assert len(args[0]) == 2
				self.x, self.y = float(args[0][0]), float(args[0][1])
		elif len(args) == 2:
			self.x, self.y = float(args[0]), float(args[1])
		else:
			raise TypeError()

	def copy(self):
		return Float2(self.x, self.y)

	def clear(self):
		self.x = 0.0
		self.y = 0.0

	def __repr__(self):
		return "Float2(%f, %f)" % (self.x, self.y)

	def __pos__(self):
		return Float2(self.x, self.y)

	def __neg__(self):
		return Float2(-self.x, -self.y)

	def __add__(self, other):
		return Float2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Float2(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		if isinstance(other, Float2):
			return Float2(self.x*other.x, self.y*other.y)
		else:
			return Float2(self.x*other, self.y*other)

	def __rmul__(self, other):
		return self.__mul__(other)		

	def __truediv__(self, other):
		if isinstance(other, Float2):
			return Float2(self.x/other.x, self.y/other.y)
		else:
			return Float2(self.x/other, self.y/other)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __imul__(self, other):
		if isinstance(other, Float2):
			self.x *= other.x
			self.y *= other.y
		else:
			self.x *= other
			self.y *= other
		return self

	def __itruediv__(self, other):
		if isinstance(other, Float2):
			self.x /= other.x
			self.y /= other.y
		else:
			self.x /= other
			self.y /= other
		return self

	def dot(self, other):
		return self.x*other.x + self.y*other.y

	def cross(self, other):
		return self.x*other.y - self.y*other.x

	def abs2(self):
		return self.x**2 + self.y**2

	def abs(self):
		return math.sqrt(self.abs2())

	def __abs__(self):
		return self.abs()

# Unittests

def _cmp(p, x, y):
	return p.x == x and p.y == y

def _iadd_cmp(a, b, x, y):
	a += b
	return _cmp(a, x, y)

def _isub_cmp(a, b, x, y):
	a -= b
	return _cmp(a, x, y)

def _imul_cmp(a, b, x, y):
	a *= b
	return _cmp(a, x, y)

def _idiv_cmp(a, b, x, y):
	a /= b
	return _cmp(a, x, y)

_ut_list = [
	utest.Unit(lambda: _cmp(Float2(), 0, 0), "__init__: 0 args"),
	utest.Unit(lambda: _cmp(Float2(1, 2), 1, 2), "__init__: 2 args"),
	utest.Unit(lambda: _cmp(Float2((2, 3)), 2, 3), "__init__: 1 args tuple"),
	utest.Unit(lambda: _cmp(Float2(Float2(3, 4)), 3, 4), "__init__: 1 args Float2"),

	utest.Unit(lambda: _cmp(+Float2(1, 2), 1, 2), "__pos__"),
	utest.Unit(lambda: _cmp(-Float2(1, 2), -1, -2), "__neg__"),

	utest.Unit(lambda: _cmp(Float2(1, 2) + Float2(3, 4), 4, 6), "__add__"),
	utest.Unit(lambda: _cmp(Float2(3, 4) - Float2(1, 2), 2, 2), "__sub__"),
	utest.Unit(lambda: _cmp(Float2(1, 2)*Float2(3, 4), 3, 8), "__mul__: Float2"),
	utest.Unit(lambda: _cmp(Float2(1, 2)*3, 3, 6), "__mul__: float"),
	utest.Unit(lambda: _cmp(3*Float2(1, 2), 3, 6), "__rmul__: float"),
	utest.Unit(lambda: _cmp(Float2(3, 4)/Float2(1, 2), 3, 2), "__div__: Float2"),
	utest.Unit(lambda: _cmp(Float2(4, 6)/2, 2, 3), "__div__: float"),

	utest.Unit(lambda: _iadd_cmp(Float2(1, 2), Float2(3, 4), 4, 6), "__iadd__"),
	utest.Unit(lambda: _isub_cmp(Float2(3, 4), Float2(1, 2), 2, 2), "__isub__"),
	utest.Unit(lambda: _imul_cmp(Float2(1, 2), Float2(3, 4), 3, 8), "__imul__: Float2"),
	utest.Unit(lambda: _imul_cmp(Float2(1, 2), 3, 3, 6), "__imul__: float"),
	utest.Unit(lambda: _idiv_cmp(Float2(3, 4), Float2(1, 2), 3, 2), "__idiv__: Float2"),
	utest.Unit(lambda: _idiv_cmp(Float2(4, 6), 2, 2, 3), "__idiv__: float"),

	utest.Unit(lambda: Float2(1, 2).dot(Float2(2, 1)) == 4, "dot: non-zero"),
	utest.Unit(lambda: Float2(1, 0).dot(Float2(0, 1)) == 0, "dot: zero"),
	utest.Unit(lambda: Float2(1, 0).cross(Float2(0, 1)) == 1, "cross: non-zero"),
	utest.Unit(lambda: Float2(1, 2).cross(Float2(1, 2)) == 0, "cross: zero"),

	utest.Unit(lambda: Float2(3, 4).abs2() == 25, "abs2"),
	utest.Unit(lambda: Float2(3, 4).abs() == 5, "abs"),
	utest.Unit(lambda: abs(Float2(3, 4)) == 5, "__abs__"),
]

def _unittest():
	utest.testall(_ut_list, verbose=True)

if __name__ == "__main__":
	_unittest()
