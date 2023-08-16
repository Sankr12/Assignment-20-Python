# Write a python program to create a function that takes a list and returns a new list 
# with the original list's unique elements

def printlist(li = []):
    unique_list = []
    for items in li:
        if items not in unique_list:
            unique_list.append(items)
    return unique_list

Original_list = [1,4,56,7,8,6,5,6,6,87,89,67,56,54,54,43,43,46,7,78]

Result_list = printlist(Original_list)
print()
print("Original List:",Original_list)
print("List with unique elements:",Result_list)
print()