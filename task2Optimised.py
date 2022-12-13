# 2. Write a program to find the list of duplicates in the list a = ['q','a','b','c','d','e','q','a','d']

a=['q','a','b','c','d','e','q','a','d']
print(list(set([x for i,x in enumerate(a) if a.count(x) > 1])))


# Time Complex: O(n)  Aux Space: O(1)