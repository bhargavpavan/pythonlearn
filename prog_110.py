# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5  
n = int(input('enter n value: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(i,n+1):
        print(n-i+1,end=" ")
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(i,n+1):
        print(n-i+1,end=" ")
    print()
