'''
     1234567
1    ___A___
2    __ABA__
3    _ABCBA_
4    ABCDCBA
'''

rows=4
col=2*rows
for i in range(1,rows+1):
    for j in range(1,col):
        if abs(rows - j) <= i - 1:
            print(chr(ord('A') + abs(rows - j)), end="")
        else:
            print("_", end="")
    print()