class MyClass(object):
    def __init__(self, number):
        self.number = number


my_objects = []

for i in range(100):
    my_objects.append(MyClass(i))

# later

for obj in my_objects:
    print(obj.number)


class SimpleClass(object):
    pass
simplelist = []
for count in range(4):
    x = SimpleClass()
    x.attr = count
    simplelist.append(x)

