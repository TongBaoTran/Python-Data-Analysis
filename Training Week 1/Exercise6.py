def triple(x):
    return x * 3


def square(x):
    return x ** 2


for i in range(1, 11):
    print(f'triple({i:2d})== {triple(i):4d} square({i:2d})== {square(i):3d}')
    if square(i) > triple(i): break
