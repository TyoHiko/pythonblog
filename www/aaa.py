import json

class Student(object):
    # name = 'aa'
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# s= Student("thr", 24, 99)
# # print(json.dumps(s, default=lambda s:s.__dict__))
# j = json.dumps(s, default=lambda s:s.__dict__)
# print(json.loads(j))
#
# print("test")

s = Student('zz', 1, 1)
print(s.name, Student.name)