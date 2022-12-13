# 2. Write a program to find the list of duplicates in the list a = ['q','a','b','c','d','e','q','a','d']

a=['q','a','b','c','d','e','q','a','d']

duplicate=[]
for i in a:
    if a.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
            
print(duplicate)
  