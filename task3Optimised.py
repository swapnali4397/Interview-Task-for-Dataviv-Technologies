# 3. Your code must return true or false depending upon whether the given number is a Narcissistic number.

def totalnum(n) :
    if (n == 0) :
        return 0
    return (1 + totalnum(n // 10))

def narcissistic(n) :
    l = totalnum(n)
    dup = n; sm = 0
    while (dup) :
        sm = sm + pow(dup % 10, l)
        dup = dup // 10
    return (n == sm)
     
n = int(input("Enter a number: "))
if (narcissistic(n)) :
    print( "true")
else :
    print( "false")   

# Time Complex: O(logn) Aux Space: O(1)