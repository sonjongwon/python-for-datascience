items = 'zero one two three'.split()  # 빈칸을 기준으로 문자열 나누기
print(items)

example = 'python,jquery,javascript'  # 콤마를 기준으로 문자열 나누기
print(example.split(","))

a, b, c = example.split(",")  # 리스트에 있는 각 값을 a, b, c 변수로 unpacking
print(a)
print(b)
print(c)

# split()를 사용하면 list 형태로 반환해줌
