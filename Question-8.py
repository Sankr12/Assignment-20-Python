# Write a python program to create a function that accepts a string and calculate the 
# number of uppercase letters and lowercase letters.

def lettercase():
    string = input("Enter a string: ")
    result1 = 0
    result2 = 0
    for characters in string:
        if 64<ord(characters)<91:
            result1+=1
        elif 96<ord(characters)<123:
            result2+=1
        else:
            pass
    print("Uppercase:",result1)
    print("Lowercase:",result2)

lettercase()