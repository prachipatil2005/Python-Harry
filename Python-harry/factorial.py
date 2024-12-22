# 5!=5x4x3x2x1
n=int(input("enter a number"))
product=1
for i in range(1,n+1):
    product*=i
print(f"the factorial of {n} is{product}")