# Write a python program to create a function to check whether a string is a pangram or not

def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()  # Convert to lowercase for case-insensitivity
    sentence = ''.join(filter(str.isalpha, sentence))  # Remove non-alphabetic characters
    sentence_set = set(sentence)
    return sentence_set == alphabet

# Test the function
input_sentence = input("Enter a sentence: ")
if is_pangram(input_sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
