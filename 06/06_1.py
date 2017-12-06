test_inputs = [[0,2,7,0]]

def distributor(l):
	indx = None
	val = 0
	for i in range(0,len(l)):
		if l[i] > val:
			indx = i
			val = l[i]
			
	l[indx] = 0

	while val > 0:
		indx = (indx + 1) % len(l)
		l[indx] += 1
		val -= 1

	return l

def allocator(l):
	s = set()
	c = 0
	while True:
		sl = len(s)
		c += 1
		l = distributor(l)
		# print(l)
		s.add(''.join(str(x) for x in l))
		if(len(s) == sl):
			break
	return c

def test():
	for i in test_inputs:
		print(allocator(i))

def answer():
	with open('06/06_input.txt') as f:
		l = []
		for ln in f:
			l = [int(x) for x in ln.split('\t')]
		print(l)
		print(allocator(l))

test()
answer()