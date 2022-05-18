#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5
n=int(input('enter n value:'))
for i in range(n,0,-1):
    for j in range(i,1,-1):
        print("  ",end="")
    for k in range(i,n+1):
        print(k,end=" ")
    print(" ")