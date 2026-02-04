'''
ABCDE
ABCD
ABC
AB
A
'''

rows=5

for i in range(0,rows):
    for j in range(0,rows-i):
        print(chr(ord('A')+j),end="")
    print("")