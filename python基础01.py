'''
# 1.打印1～100内的偶数
for i in range(1,100):
	if i%2==0:
		print(i)

# 2.从键盘获取用户名、密码，如果用户名和密码都正确，显示“欢迎登陆xxx”，否则提示密码或者用户名错误
r_username = "zust"
r_passwd = "123456"
username = input(">>> ")
passwd = input(">>> ")
if username == r_username and passwd == r_passwd:
    print("欢迎登陆%s"%username)
else:
    print("输入有误")

# 3.从键盘接收一百分制成绩（0~100），要求输出其对应的成绩等级A~E。其中，90分以上为'A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'。
usergrade = input("请输入成绩>>")
if usergrade.isdigit() is True:
    if int(usergrade)>=90:
        print("A")
    elif int(usergrade)>=80:
        print("B")
    elif int(usergrade)>=70:
        print("C")
    elif int(usergrade)>=60:
        print("D")
    else:
        print("E")
else:
    print("请输入数字")


# 4.计算从1加到end，变量end的值由键盘输入。假如输入end的值为6，则代码输出的结果应该是21，也就是1+2+3+4+5+6的结果
num=int(input("please input a number:"))
sum=0
i=0
while i<=num:
	sum=sum+i
	i+=1
print(sum)


# 5.打印九九乘法表
i=1
while i<=9:
	j=1
	while j<=i:
		mult=i*j
		print("%d*%d=%d "%(i,j,mult),end="")
		j+=1
	i+=1
	print("\n")




# 6.200内被17整除的最大正整数
num=200
while num>0:
	if num%17==0:
		print(num)
		break
	num-=1


# 7.100以内的所有素数
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

# 9.输入一个分钟数，转换成小时和分钟

# 10.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

# 11.设计一个复利计算函数invest()，它包含三个参数：amount（资金），rate（利率），time（投资时间）。输入每个参数后调用函数，应该返回每一年的资金总额。

# 12.编写函数，输入一个正整数n，求1！+2!+...+n!

# 13.通过递归函数实现计算1到100相加之和

# 14.利用递归函数调用的方式，将输入的字符以相反顺序输出



'''