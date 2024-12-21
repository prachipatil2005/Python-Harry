n=int(input("enter a number"))
if n<=1:
    print(f"{n} is not a prime number")
else:
 for i in range(2,n):
    if(i%2==0):
        print(f"{n}number is not prime")
        break
 else:
    print("number is prime")