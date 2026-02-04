'''
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''

# printing this as 2 patters combined together 
total_rows=8
pt1row=total_rows//2
pt2row=total_rows//2

for i in range(0,pt1row):
    #rightspaces
    for j in range(0,pt1row-i-1):
        print(" ",end="")
    #stars
    for j in range(0,2*i+1):
        print("*",end="")
    print("")

#printing pattern2 
for i in range(pt2row, 0, -1):
    # left spaces
    for j in range(pt1row - i):
        print(" ", end="")
    
    # stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()