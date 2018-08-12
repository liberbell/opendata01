r = range(0, 30)
print(type(r))
print(type(10))
print(type('a'))
print(type('Hi there'))

class cars:
    pass

class Trucks():
    pass

c = cars()
convert = cars()
t = Trucks()

print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(convert))

print(isinstance(c, cars))
print(isinstance(t, cars))

if isinstance(r, range):
    print(list(r))
