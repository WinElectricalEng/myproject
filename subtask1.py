def myFindSquare(n):
    b = 0
    a = 1
    # if a squre is bigger than the number then 
    # we break out from the while loop
    while(b**2 > n or n >= a**2 ):
        #as long as the while condition is true, keep adding a and b
        b = b + 1
        a = a + 1
    #after break out from loop calculate final q
    q = b**2
    print("q is: ", b, "\n""q^2 is: ",q )

myFindSquare(40)