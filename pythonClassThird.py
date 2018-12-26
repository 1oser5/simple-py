#1统计单词
# str=input('enter word');
# count=0;
# for i in str:
#     if(i!=' '):
#         count+=1;
# print(count);

#2垃圾分类
# str=input('enter your key')
# numCount=0
# strCount=0
# elseCount=0
# for i in str:
#     if i.isalpha():
#         strCount+=1
#     elif i.isdigit():
#         numCount+=1
#     else:
#         elseCount+=1
# print(numCount,strCount,elseCount)

#3计算器
# str=input('enter colmon')
# ary=(str.split('+'))
# sum=0
# for i in ary:
#     sum+=int(i)
# print(sum)

#4找不同
# L1=['1','2','3','4']
# L2=['1','3','4','5']
# sum=L1+L2
# result=[]
# for i in sum:
#     if sum.count(i)!=1:
#         result.append(i)
# print(result)

#5去重
# L2=[1,2,3,3,4,5,6,7,2,3];
# S1=list(set(L2))
# print(S1)

#6
# L1=['1','2','3','4']
# L2=['1','3','4','5']
# sum=L1+L2
# result=[]
# for i in sum:
#     if sum.count(i)!=1:
#         result.append(i)
# print(result)

#7数字字典
D1={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'};
num=input('enter number');
for i in num:
    print(D1[i],end="")