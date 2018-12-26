def triangles():
	L=[1]
	while(True):
		yield L
		M = [ L[x]+L[x+1] for x in range(len(L)-1)]
		L=[1]+M+[1]
