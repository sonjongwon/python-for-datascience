def asterisk_test_1(a, *args):
    print(a, args)
    print(type(args))


asterisk_test_1(1, *(2, 3, 4, 5, 6))


def asterisk_test_2(a, args):
    print(a, *args)
    print(type(args))


asterisk_test_2(1, (2, 3, 4, 5, 6))

# unpacking a container

x, y, z = ([1, 2], [3, 4], [5, 6])
print(x, y, z)

data_1 = ([1, 2], [3, 4], [5, 6])
print(*data_1)
# 18 ~ 22번째 줄은 같은 결과를 보여줌

for data_2 in zip([1, 2], [3, 4], [5, 6]):
    print(data_2)


def asterisk_test_3(q, w, e, r):
    print(q, w, e, r)


data_3 = {"w": 1, "e": 2, "r": 3}
asterisk_test_3(10, **data_3)
