class Student(object):
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Class Student,name:%s'%(self._name)
print(Student('Orangary'))
    