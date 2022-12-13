# 1. Write a program to count the number of each character in the word “success”?
import string
 
a = 'success'
res = len([ele for ele in a if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
print("Count of Alphabets : " + str(res))

# Time Complex: O(n)  Aux Space: O(n)