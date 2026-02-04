'''
*****
 ***
  *
'''

n = 3

for i in range(n, 0, -1):
    # left spaces
    for j in range(n - i):
        print(" ", end="")
    
    # stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()
