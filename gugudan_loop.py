print("구구단 몇 단을 계산할까요(1~9)?")
print("0을 입력시 게임은 종료됩니다.")
x = True

while x != 0:
    x = int(input())
    if x == 0:
        break
    elif 1 <= x <= 9:
        print("구구단", str(x), "단을 계산합니다.")
        for i in range(1, 10):
            print(str(x), "X", i, "=", x*i)
    else:
        print("잘못 입력하셨습니다. 1부터 9사이의 숫자를 입력해주세요.")
    print("구구단 몇 단을 계산할까요(1~9)?")
print("구구단 게임을 종료합니다.")
