#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
	if len(L)==0:		#长度为0则返回None
		return(None,None)
	else:
		min=max=L[0]
		for index in L:
			if index<min:	
				min=index
			if index>max:
				max=index
		print(min,max)
		return (min,max)

findMinAndMax([3,2,1])