#0
# print(("姓名：{0},电话:{1},邮箱:{2}").format('xtl','110','qq@'))


#1 直接print失败
# print(list(range(2,100,2)))

#2
# name=input('enter your name')
# psd=input('enter your psd')
# if name=='xtl':
# 	if psd=='snoopy':
# 		print('success')
# 	else:
# 		print('wrong psd')
# else:
# 	print('wrong name')

#3
# score=int(input('enter score '))
# if score>100|score<1:
# 	print('wrong range')
# else:
# 	if score>90:
# 		print('A')
# 	elif  score>80:
# 		print('B')
# 	elif  score>70:
# 		print('C')
# 	elif  score>60:
# 		print('D')
# 	else:
# 		print('E')

#4
# end=int(input('enter end '))
# sum=0
# for num in range(1,end+1):
# 	sum+=num
# 	num+=1
# print(sum)


#5
# for left in range(1,10):
# 	for right in range(1,10):
# 		print('{}*{}={}'.format(left,right,left*right),end=' ')
# 	print('') 

#6
# for num in range(1,200):
# 	if num%17==0:
# 		sum=num
# print(sum)

#7
count=0
num=2
while num<100:
	col=1
	i=2
	while i<num:
		if num%i==0:
			col=0
			break
		i+=1
	if col==1:
		print(i)
		count+=1
	num+=1
print("一共有："+str(count))

# 8.连续输入数字并计算平均分
sum=0
num=0
col="y"
while col=="y":
	score=int(input("please input a number:"))
	sum=sum+score
	num+=1
	avg=sum/num
	print(avg)
	col=input("would you like to go on?(y/n)")