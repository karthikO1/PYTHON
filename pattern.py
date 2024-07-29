n=int(input("enter no of rows: "))
for i in range(0,n+1):
    for j in range(n,0,-1):
        if(j>i):
            print("*",end=" ")
    print("\n")    
