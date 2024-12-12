n=int(input("enter a number"))
for i in range(2,n):
    if(i%2==0):
        print("number is not prime")
        break
else:
    print("number is prime")