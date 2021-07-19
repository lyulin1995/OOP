# x = {'key': 4}
# x['key2'] = 5
# x[3] = [1,4,5]
# for key, value in x.items():
#     print(key, value)
# for key in x:
#     print(key, x[key])
#
# y = [[0 + y for y in range(10)] for y in range(5)]
# print(y)
# z = [i for i in range(100) if i % 5 == 0]
# print(z)

# def func1(x, y, z=None):
#     print('Run', x, y, z)
#     return x * y, x / y
#
#
# r1, r2 = func1(5, 6, 7)
# print(r1, r2)

# def func(x):
#     def func2():
#         print(x)
#
#     return func2
#
# # print(func(3)())
# x = func(3)
# x()
# print(x)

# def func(x, y):
#     print(x, y)
# pairs = [(1,2), (3,4)]
#
# for pair in pairs:
#     func(*pair)
#
# for pair in pairs:
#     func(**{'x':2, 'y':5})
#
# def func(*args, **kwargs):
#     print(args, kwargs)
#     print(*args)
#
# func(1, 2, 3, 4, 5, one=0, two=1)

## x is a local variable with in the scope of this function (below)
## the name does not change since is local variable
# x = 'tim'
#
# def func(name):
#     x = name
#
# print(x)
# func('changed')
# print(x)

## global x

# x = 'tim'
#
# def func(name):
#     global x
#     x = name
#
# print(x)
# func('changed')
# print(x)

# raise Exception('Bad')
# try:
#     x = 7 / 0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

# x = lambda x, y: x + y
# print(x(2, 32))

# x = [1, 2, 4, 5, 3, 3, 21, 2, 21, 2, 313, 1, 23, 142, 4]
#
# mp = map(lambda i: i + 2, x)
# print(list(mp))
#
# fl = filter(lambda i: i % 2 == 0, x)
# print(list(fl))
#
#
# def func(i):
#     i = i * 3
#     return i % 2 == 0
#
#
# fl1 = filter(func, x)
# print(list(fl1))

