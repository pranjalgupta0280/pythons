def is_armstrong_number(num):
    temp = num
    power = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num