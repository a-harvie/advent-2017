import math
from pprint import pprint

answer_input = 368078
test_inputs = [[1,1],[2,1],[3,2],[4,4],[5,5]]
# test_inputs = [[1,1]]
# # test_inputs = [[2,1]]
# # test_inputs = [[3,2]]
# # test_inputs = [[4,4]]
# test_inputs = [[5,5]]

g = []

def initializeGrid(size):
	global g
	g = []
	for i in range(0, size*2+1):
		l = [0] * ((size*2)+1)
		g.append(l)

	print('grid is {0}sq'.format(size*2+1))

def makeSpiral(grid_size, max_val=None, max_moves=None):
	pos = [grid_size,grid_size]
	vec = [1,0]
	val = 1
	g[pos[0]][pos[1]] = val
	# pprint(g)
	turn_c = 0
	turn_i = False
	turn_g = 2

	i = 1
	while True:		
		pos = [pos[0] + vec[0], pos[1] + vec[1]]
		val = gridSum(pos)
		# print(val)
		# pprint(g)
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
		i += 1
		if i >= max_moves:
			break
		if val > max_val:
			break

		
	# print(val)
	# return int(math.fabs(pos[0]) + math.fabs(pos[1]))
	return (val,i)

def gridSum(pos):
	# print('gs',pos)
	x = pos[0]
	y = pos[1]
	s = 0
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			# print(i,j)
			s += g[i][j]

	g[x][y] = s
	return s

def turnVec(vec):
	rm = [[0,-1],[1,0]]
	return [vec[0]*rm[0][0] + vec[1]*rm[0][1], vec[0]*rm[1][0] + vec[1]*rm[1][1]]


def test():
	for i in test_inputs:
		print(i, i[0])
		initializeGrid(i[0]*2)
		s = makeSpiral(i[0]*2,10000,i[1])
		print(s)


def answer():
	gs = 1000
	initializeGrid(gs)
	print(makeSpiral(gs,answer_input,1000000))

# test()
answer()