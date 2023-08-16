# Write a python program to create a function to find the min of three numbers

def minimun():
    li = []
    for i in range(3):
        num = int(input("Enter number {}: ".format(i+1)))
        li.append(num)
    print("Minimum of your given three numbers {}, {}, {} is {}".format(li[0],li[1],li[2],min(li)))

minimun()