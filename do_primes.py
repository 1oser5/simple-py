####找素数
##无限迭代器，跳跃间隔为2，去掉所有素数
# def do_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n

# def do_disvisible(n):
#         return lambda x:x%n>0
# def primes():
#      it = do_iter()  #初始化序列
#      while True:
#         n = next(it)
#         yield n
#         it = filter(do_disvisible(n),it)
# for i in primes():
#     if i <1000:
#         print(i)
#     else:
#         break


####找回数
#1
def is_palindrome(n):
    rev = 0
    while rev<n:
        rev = rev*10+n%10
        n = int(n/10)
        print(n)
        print(rev)
    return (n==rev or n==int(rev/10))

#2
# def is_palindrome(n):
#     return str(n)==str(n)[::-1]

print(is_palindrome(12321))