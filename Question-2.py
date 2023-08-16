# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not

def prime_number():
    num = int(input("Enter a number: "))
    if num<2:
        print(num,"is not a prime number")
    else:
        for i in range(2,num):
            if num%i==0:
                print("{} is not a prime number".format(num))
                break
        else:
            print("{} is a prime number".format(num))

prime_number()