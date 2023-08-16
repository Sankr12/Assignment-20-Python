# Write a python program to create a function that prints the even number from the given list
# Sample list: [1,2,3,4,5,6,7,8,9]

def print_even():
    sample_list = [1,2,3,4,5,6,7,8,9]
    for items in sample_list:
        if items%2==0:
            print(items)

print_even()