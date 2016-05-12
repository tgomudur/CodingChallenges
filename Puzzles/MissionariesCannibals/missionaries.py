def isValidMove(state, capacity):
	i, j, _ = state
	if (i == 0 and j == 0) or i + j > capacity or j > i:
		if i == 0 and j > i and not i + j > capacity :
			return True
		return False
	else:
		return True

def generateAllPossibleMoves(state, capacity):
	M, C , direction= state
	allmoves = []
	for i in range(M+1):
		for j in range(C+1):
			if isValidMove((i, j, direction), capacity):
				allmoves.append((i, j, direction))
	return allmoves

def bfs_path(start):
	stop_limit = 0
	M, C, capacity = start
	initdirection = 1
	queue = [((M, C, initdirection), [(M, C, initdirection)])]
	count = 0 
	goalReached = False
	direction = initdirection
	visited = set()
	while queue:
		(vertex, path) = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
		else:
			continue
		count += 1
		if vertex[2] == 0:
			v = (M-vertex[0], C - vertex[1], vertex[2])
		else:
			v = vertex
		allmoves = generateAllPossibleMoves(v, capacity)
		# print "Vertex {}".format(vertex)
		# print "AllMoves: {}".format(allmoves)
		for i, j, k in allmoves:
			if k == 1:
				newState = (vertex[0] - i, vertex[1] - j, 0)
			else:
				newState = (vertex[0] + i, vertex[1] + j, 1)
			if check(newState, M, C):
				if newState == (0, 0, 0):
					print "Success"
					return path + [newState]
				else:
					new_path = [(newState, path + [newState])]
					queue = queue + new_path
			
def check(newState, M, C):
	# print newState
	if newState[0] > M or newState[1] > C or (newState[0] == M and newState[1] == C): return False
	if (newState[1] and newState[0] and  newState[1] > newState[0]): return False
	if (C - newState[1] > M - newState[0] and C - newState[1] and M - newState[0]): return False
	return True
	
def main():
	states = bfs_path((3,3,2))
	if moves:
		print moves
	else:
		print "Failed: Task is not possible"

if __name__ == '__main__':
	main()