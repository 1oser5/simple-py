import pickle
#二进制存入文件
# d = dict(name = 'snoopy', age = 20, score = 88)
# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

import json
#从文件中读取
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
# print(d)

#json读取
d = dict(name = 'snoopy', age = 20, score = 88)
#json.dumps将字典类型转化为json字符串！ 序列化
d_str = json.dumps(d)
# print(type(d_str)) #<class 'str'>
#反序列化
d_json= json.loads(d_str)
# print(d_json)

#转化json类
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
#序列化
# print(json.dumps(s, default=lambda obj: obj.__dict__))
#定义反序列化函数
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}' 
#反序列化   
# print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
obj = dict(name='bob', age=20)
#ensure_ascii,中文存储为ascii编码
s = json.dumps(obj, ensure_ascii=True)
print(s)
