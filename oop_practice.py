class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} 在汪汪叫")


class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def multiply(self, num1, num2):
        return num1 * num2

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count
    def reset(self):
        self.count = 0





dog = Dog("小强","金毛")
