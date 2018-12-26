def move(n,a,b,c):
	if n==1:
		print(a,'->',c)	#如果n==1，就直接移至c
	else:
		move(n-1,a,c,b) 	#把a盘的n-1个盘子借助c盘移动到b盘
		move(1,a,b,c)		#把a最下面的盘子借助b移动到c位置
		move(n-1,b,a,c)		#把b盘的n-1盘子借助a移动到c

move(4,"A","B","C")