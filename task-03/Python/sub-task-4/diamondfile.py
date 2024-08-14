with open('input.txt','r') as infile:
    n = int(infile.read())
x=n//2
y=n//2+1
diamond=[]

for i in range(x):
    line =" "*(x-i)+"*"*(i+1)+"*"*i
    diamond.append(line)

for j in range(y,0,-1):
    line =" "*(y-j)+"*"*j+"*"*(j-1)
    diamond.append(line)

with open('output.txt', 'w') as outfile:
    outfile.write('\n'.join(diamond))