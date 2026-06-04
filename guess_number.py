import random

target = random.randint(1, 100)
attempts = 0

print("猜数字游戏：我心里想了一个1-100之间的数字，你猜猜看？")

while True:
    input_value = input("请输入一个数字: ")
    attempts += 1

    try:
        input_value = int(input_value)
    except ValueError:
        print("请输入一个有效的数字！")
        continue

    if input_value == target:
        print(f"恭喜你猜对了！你一共猜了{attempts}次。")
        break
    elif input_value > target:
        print("输入的数字偏大")
    else:
        print("输入的数字偏小")