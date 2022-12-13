# 1. Write a program to count the number of each character in the word “success”?

string = input("Enter a string: ")

print("operation to be performed: 1 - Total lenght 2 - count of a specific character")
choice = input()

if choice == "1":
    print("Total length is: ", len(string))
elif choice == "2":
    char = input("Enter the character to be counted: ")
    if char in string:
        print("Count of the character is: ", string.count(char))
    else:
        print("Character not found in the string")
else:
    print("Invalid choice...")