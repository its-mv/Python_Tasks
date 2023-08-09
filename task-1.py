a = int(input("Enter number to print fibo series : "))

def fibon(a):

    if(a<=1):
        return 1
    return fibon(a-1)+fibon(a-2)

i = 0

while (i<a):
    print ( fibon(i) )
    i +=1

