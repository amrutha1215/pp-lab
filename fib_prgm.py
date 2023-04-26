n=int(input("enter number of terms : "))
a,b=0,1
count=0

if n<=0:
    print("enter a positive integer")

elif n==1:
    print("fibinocci sequence upto {}:".format(n))
    print(a)
else:
    print("fibonacci sequence:")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
        
