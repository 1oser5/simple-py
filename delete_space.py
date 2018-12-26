#删除首尾空格

def trim(s):
	while s[0]==" ":
		if s[0]==" ":
			#print("in1")
			s=s[1:]
		if s[-1]==" ":
			#print("in2")
			s=s[:-1]
	return s
print(trim("   hello          "))

