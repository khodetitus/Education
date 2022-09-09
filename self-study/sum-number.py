def sum_number(number):
    total_number = 0
    for num in range(1, number + 1):
        total_number += num
    return total_number


print(sum_number(5))  # 1+2+3+4+5
