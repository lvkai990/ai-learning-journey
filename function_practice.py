def get_name(name):
    return name

res = get_name("王晓晓")
print(res)


def say_hello():
    return "Hello Python!"

print(say_hello())



def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(1,2,3))

def is_even(number):
    return number % 2 == 0
print(is_even(3))