with open("test.txt", "r", encoding="utf-8") as f:
    #f.write("Hello World")
    red_line_content = f.readline()

    print(red_line_content)