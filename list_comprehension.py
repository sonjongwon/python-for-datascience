# General Style
result = []
for i in range(10):
    result.append(i)
print(result)

# List comprehension(1/4)
results_1 = [i for i in range(10)]
print(results_1)
results_1 = [i for i in range(10) if i % 2 == 0]
print(results_1)

# List comprehension(2/4)
word_1 = "Hello"
word_2 = "World"
result_2 = [i+j for i in word_1 for j in word_2]
# Nested for loop
print(result_2)

# List comprehension(3/4)
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result_3 = [i+j for i in case_1 for j in case_2]
print(result_3)
result_3 = [i+j for i in case_1 for j in case_2 if not i == j]
print(result_3)
print(sorted(result_3))

# List comprehension(4/4)
words = "The quick brown fox jumps over the lazy dog".split()  # 문장을 빈칸 기준으로 나눠서 list 형태로 변환
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

# Two dimensional vs One dimensional
case_3 = ["A", "B", "C"]
case_4 = ["D", "E", "A"]
result_5 = [i+j for i in case_3 for j in case_4]
print(result_5)
result_5 = [[i+j for i in case_3] for j in case_4]
# Nested for loop 이지만 for j in case_4가 위에 있음
