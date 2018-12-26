def createCounter():
    a=[0]
    def counter():
        a[0]+=1
        return  a[0]
    return counter
f = createCounter()
print(f())
print(f())
print(f())
print(f())
