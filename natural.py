def sum(n):
    if(n==1):#base condition
        return 1
    else:
        return sum(n-1)+n
n=int(input("enter a number:"))
print(sum(n))