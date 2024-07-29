n=int(input("enter the number: "))
rev=n
sum=0
while n>0:
    b=n%10
    sum=sum*10+b
    n=n//10
if (rev==sum):
    print(f"{rev} is palindrome")
else:
    print(f"{rev} is not a palindrome")
