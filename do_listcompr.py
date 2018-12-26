L1 = ['Hello', 'World', 18, 'Apple', None]

L=[x.lower() for x in L1 if isinstance(x,str)]	

print(L)