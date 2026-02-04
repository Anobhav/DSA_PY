'''
A
AB
ABC
ABCD
ABCDE
'''
rows=5
for i in range(1,rows+1):
    for j in range(i):
        print(chr(ord('A')+j),end="")
    print("")