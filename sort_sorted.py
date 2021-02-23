list_test = [5, 4, 3, 2, 1]
print(list_test.sort())
#  None 이 나오는 이유는 return 값이 없기 때문

list_test = [5, 4, 3, 2, 1]
list_test.sort()
print(list_test)
# [1, 2, 3, 4, 5]가 잘 나오는 이유는 return 값은 없지만 리스트 자체를 sorting 시켰기 때문

list_test = [5, 4, 3, 2, 1]
print(sorted(list_test))
