import browser

cnv = browser.document["canvas"]
ctx = cnv.getContext("2d")

class Float2:
	def __init__(self, *args):
		if len(args) == 0:
			self.x, self.y = 0.0, 0.0
		elif len(args) == 1:
			try:
				self.x, self.y = float(args[0].x), float(args[0].y)
			except AttributeError:
				assert len(args[0]) == 2
				self.x, self.y = float(args[0][0]), float(args[0][1])
		elif len(args) == 2:
			self.x, self.y = float(args[0]), float(args[1])
		else:
			raise TypeError()

	def __str__(self):
		return "Float2(%f, %f)" % (self.x, self.y)

class _Unittest:
	def __init__(self, func, info):
		self.func = func
		self.info = info

	def test(self):
		try:
			v = self.func()
		except:
			return False
		return v

def _cmp(p, x, y):
	return p.x == x and p.y == y

_unittest_Float2 = [
	_Unittest(lambda: _cmp(Float2(), 0.0, 0.0), "__init__: 0 args"),
	_Unittest(lambda: _cmp(Float2(1, 2), 1.0, 2.0), "__init__: 2 args"),
	_Unittest(lambda: _cmp(Float2((2, 3)), 2.0, 3.0), "__init__: 1 args tuple"),
	_Unittest(lambda: _cmp(Float2(Float2(3, 4)), 3.0, 4.0), "__init__: 1 args Float2"),
]

_cnt = 0
_fstr = ["fail", "ok"]
_verbose = True
for ut in _unittest_Float2:
	v = ut.test()
	if not v or _verbose:
		print("[%s] %s" % (_fstr[v], ut.info))
	_cnt += not v
print("[%s] %d tests failed" % (_fstr[_cnt == 0], _cnt))

print("main.py loaded")
