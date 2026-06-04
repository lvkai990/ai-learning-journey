import datetime

def write_diary():
    content = input("请输入日记内容: ")
    if not content.strip():
        print("内容不能为空，日记未保存。")
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("rj.txt", "a", encoding="utf-8") as f:
        f.write(f"{now}: {content}\n")
    print("日记已保存！")

def read_diary():
    try:
        with open("rj.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content.strip():
                print("======== 日记列表 ========")
                print(content)
            else:
                print("日记文件为空。")
    except FileNotFoundError:
        print("还没有写过日记，请先写一篇吧。")

def main():
    while True:  # 循环放在这里
        print("\n========= 记事本 =========")
        print("1. 写日记")
        print("2. 读日记")
        print("3. 退出")
        option = input("请选择: ")

        if option == "1":
            write_diary()
        elif option == "2":
            read_diary()
        elif option == "3":
            print("再见！")
            break  # 退出循环
        else:
            print("输入有误，请重新选择。")

#if __name__ == '__main__':
#    main()
