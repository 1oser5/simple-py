# 9.输入一个分钟数，转换成小时和分钟
def translate(n):
	print(n*60,'s')
	print(n/60,'h')
# translate(15)
# 10.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def jugdeNum(n):
	while n>0:
		return 1/n+jugdeNum(n-2) 
	return 0
# print(jugdeNum(5))
# 11.设计一个复利计算函数invest()，它包含三个参数：amount（资金），rate（利率），time（投资时间）。输入每个参数后调用函数，应该返回每一年的资金总额。
def invest(amount,rate,time):
		return amount*(1+rate)*time
# print(invest(1,2,3))
# 12.编写函数，输入一个正整数n，求1！+2!+...+n!
def loop(n):
	def addNum(index):
		while index>0:
			return index*addNum(index-1)
		return 1
	sum=0
	for index in range(1,n+1):
		sum+=addNum(index)
	print(sum)
# loop(3)
# 13.通过递归函数实现计算1到100相加之和
def addOne(n):
	while n>0:
		return n+addOne(n-1)
	return 0
# print(addOne(100))
# 14.利用递归函数调用的方式，将输入的字符以相反顺序输出
def reverse(str):
	while len(str)>0:
		print(str[-1],end='')
		return reverse(str[:-1])
	return ''
# print(reverse('abc'))