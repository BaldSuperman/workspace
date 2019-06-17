def choose_class(name):
    if name =='foo':
        class FOO(object):
            pass
        return FOO
    else:
        class Bar(object) :
            pass
        return Bar
MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

