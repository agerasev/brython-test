#import traceback

class Unit:
	def __init__(self, func, info):
		self.func = func
		self.info = info
		self.trace = ""

	def test(self):
		try:
			v = self.func()
		except:
			#self.trace = traceback.format_exc()
			return False
		return v

def testall(ut_list, verbose=False):
	cnt = 0
	fstr = ["fail", "ok"]
	for ut in ut_list:
		v = ut.test()
		if not v or verbose:
			print("[%s] %s" % (fstr[v], ut.info))
			if len(ut.trace) > 0:
				print(ut.trace)
		cnt += not v
	print("[%s] %d tests failed" % (fstr[cnt == 0], cnt))