# List의 element를 추출할 때 index의 번호를 붙여서 추출
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# list의 있는 index와 값을 unpacking

my_list = ["a", "b", "c ", "d"]
print(list(enumerate(my_list)))  # list의 있는 index와 값을 unpacking하여 list로 저장

# 문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장
print({i: j for i, j in enumerate("Gachon University is an academic institute located in South Korea".split())})
