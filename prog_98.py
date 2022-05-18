# 1 2 3 4 5
#   2 3 4 5
#     3 4 5
#       4 5
#         5

n=int(input('enter n value:'))
for i in range(1,n+1):
    for j in range(1,i):
        print("  ",end="")
    for k in range(i,n+1):
        print(k,end=" ")    
    print(" ")