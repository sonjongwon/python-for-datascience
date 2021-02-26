colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors)  # 연결 시 빈칸 1칸으로 연결
print(result)

result = ', '.join(colors)  # 연결 시 ", "으로 연결
print(result)

result = '-'.join(colors)  # 연결 시 "-"으로 연결
print(result)

# join()를 사용하면 string 형태로 반환해줌
