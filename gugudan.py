print("구구단 몇 단을 계산할까요?")
user_input = input()
print("구구단", user_input, "단을 계산합니다.")
for i in range(1, 10):
    print(user_input, "X", i, "=", int(user_input)*i)
