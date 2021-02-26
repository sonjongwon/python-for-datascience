# 두개의 list의 값을 병렬적으로 추출함
a_list = ["a1", "a2", "a3"]
b_list = ["b1", "b2", "b3"]

for a, b in zip(a_list, b_list):
    print(a, b)  # 병렬적으로 값을 추출함

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)  # 각 tuple의 같은 index 끼리 묶음

print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])
# 각 tuple의 같은 index를 묶어 합을 list로 변환

# Enumerate & Zip
list_a = ["a1", "a2", "a3"]
list_b = ["b1", "b2", "b3"]

for i, (a, b) in enumerate(zip(list_a, list_b)):
    print(i, a, b)  # index list_a[index], list_b[index]로 표시
