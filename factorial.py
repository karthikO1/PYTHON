n=int(input("Enter the number to find factorial: "))
f=1
for i in range(1,n+1):
    f=f*i
    
print(f"The factorial value of {n} is: {f}")
