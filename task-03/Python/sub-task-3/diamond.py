n=int(input())
x=n//2
y=n//2+1

for i in range(x):
    print(" "*(x-i)+"*"*(i+1)+"*"*i)

for j in range(y,0,-1):
    print(" "*(y-j)+"*"*j+"*"*(j-1))