# 3. Your code must return true or false depending upon whether the given number is a Narcissistic number.

n=input("Enter a number: ")
m=int(n)
s=0
q=m
while(m!=0):
    p=m%10
    s+=p**(len(n))
    m=m//10
if(s==q):
    print('true')
else:
    print('false')