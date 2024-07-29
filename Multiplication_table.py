#using while loop

n=int(input("Enter the multiplication table of:"))
t=int(input("Enter no of terms:"))
i=1
while i<=t:
    print(f'{n} * {i} = {n*i}')
    i+=1

#using for loop

n=int(input("Enter the multiplication table of:"))
t=int(input("Enter no of terms:"))
for i in range(1,t+1):
    print(f'{n} * {i} = {n*i}')

