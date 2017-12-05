test_inputs = [[0,3,0,1,-3]]

def jumps(l):
	v = None
	c = 0
	i = 0
	while True:
		print(i,c,v)
		try:
			v = l[i]
			l[i] += 1
			i += v
			c += 1
		except Exception as e:
			print("done")
			break

	return c

def test():
	for i in test_inputs:
		print(jumps(i))

def answer():
	with open('05/05_input.txt') as f:
		l = []
		for ln in f:
			l.append(int(ln))
		print(jumps(l))

test()
answer()