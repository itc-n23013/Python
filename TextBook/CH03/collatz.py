def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    number = int(input("整数を入力してください: "))
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print("有効な整数を入力してください。")
