# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30

def squares():
    l1 = []
    for i in range(2,30):
        a = i*i
        l1.append(a)
    print(l1)

squares()