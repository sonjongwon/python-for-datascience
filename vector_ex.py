u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)]
print(result)

# Scalar-Vector Product

u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha * sum(t) for t in zip(u, v)]
print(result)
# 2 * ([1, 2, 3] + [4, 4, 4]) = 2 * [5, 6, 7] = [10 ,12, 14]과 같음
