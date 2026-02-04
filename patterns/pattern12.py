'''
1______1
12____21
123__321
12344321
'''

rows=4
col=2*rows

for i in range(1,rows+1):
    for j in range(1,col+1):
        if(j<=i):
            print(j,end="")
        elif(j<=col-i):
            print(end="_")
        else:
            print(col - j + 1,end="")
    print()