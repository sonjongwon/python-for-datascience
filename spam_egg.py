def spam(eggs):
    eggs.append(1)
    print(ham)
    eggs = [2, 3]
    print(eggs)


ham = [0]
spam(ham)
print(ham)

# call by reference 라는 함수 호출 방식
# call by value 함수 호출 방식을 사용하는 것이 좋음
