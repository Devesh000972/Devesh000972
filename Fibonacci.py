# fibbonachi sequense
def f (n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (n-1) + (n-2)
        
i = int (input ('Enter the number:'))
print (f(i))