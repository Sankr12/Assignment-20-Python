# Write a python program to access a function inside a function

def func(num):
    return num*num

def squares():
    number = int(input("Enter the number: "))
    result = func(number)
    return result

a = squares()
print("The Square is {}".format(a))