n=int(input("enter the number: "))
rev=n
sum=0
while n>0:
    a=n%10
    sum+=(a*a*a)
    n=n//10
if (rev==sum):
    print(f"{rev} is armstrong number")
else:
    print(f"{rev} is not a armstrong number")
