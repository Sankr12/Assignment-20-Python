# Write a python program to create a function to check whether a string is an anagram or not.

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Test the function
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if is_anagram(input_str1, input_str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
