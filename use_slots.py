from types import MethodType
class Stundent(object):
    __slots__= ('name','show_msg')
s = Stundent()
s.name = 'orangary'
print(s.name)

def show_msg(self):
    print('im in')

s.show_msg = MethodType(show_msg,s)
s.show_msg()