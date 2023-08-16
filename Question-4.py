# Write a python program to create a function that checks whether a passed string is palindrome or not

def palindrome_string():
    string = input("Enter a string: ")
    if string[::] == string[::-1]:
        print("{} is a palindrome".format(string))
    else:
        print("{} is not a palindrome".format(string))

palindrome_string()