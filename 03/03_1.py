import math

answer_input = 368078
test_inputs = [[1,0],[12,3],[23,2], [1024,31]]

def makeSpiral(len):
	pos = [0,0]
	vec = [1,0]
	out = [[0,0]]
	turn_c = 0
	turn_i = False
	turn_g = 2
	for i in range(1,len):
		pos = [pos[0] + vec[0], pos[1] + vec[1]]
		# print(i, pos, vec)

		if i == 1 or i == 2:
			vec = turnVec(vec)
			# print('t', vec)
		elif i > 2 and turn_c == turn_g:
			turn_c = 0
			if(turn_i):
				turn_g += 1
				turn_i = False
			else:
				turn_i = True
			vec = turnVec(vec)
			# print('tt', vec)
		if i >= 2:
			turn_c += 1
		
	print(pos)
	return int(math.fabs(pos[0]) + math.fabs(pos[1]))

def turnVec(vec):
	rm = [[0,-1],[1,0]]
	return [vec[0]*rm[0][0] + vec[1]*rm[0][1], vec[0]*rm[1][0] + vec[1]*rm[1][1]]

def test():
	for i in test_inputs:
		print(i)
		print(i[0])
		s = makeSpiral(i[0])
		print('{0} {1}'.format(s, s == i[1]))

def answer():
	print(makeSpiral(answer_input))

test()
answer()