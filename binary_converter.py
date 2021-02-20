print("input decimal number:")
decimal = int(input())
result = ''
loop_counter = 0
while decimal > 0:
    temp_decimal_input = decimal
    temp_result_input = result

    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result

    print("----------", loop_counter, "loop value check----------")
    print("initial decimal:", temp_decimal_input,
          ", Remainder:", remainder,
          ", initial_result:", temp_result_input)
    print("Output decimal:", decimal,
          "Output_result:", result)
    print("-"*50)
    print("")

    loop_counter += 1
print("Binary number is", result)
