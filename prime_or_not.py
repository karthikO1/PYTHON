n=int(input("enter the number: "))
i=1
flag=0
cnt=0
if(n==1):
    print(f"{n} is not a prime")
else:
    while i<=n:
        if(n%i==0):
            cnt+=1
            if(cnt>2):
                flag=1
                break
        i+=1
    if flag==1:
        print(f"{n} is not a prime")
    else:
        print(f"{n} is a prime")
