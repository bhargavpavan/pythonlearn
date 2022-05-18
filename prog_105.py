#         5
#       4 4
#     3 3 3
#   2 2 2 2
# 1 1 1 1 1
n=int(input('enter n value:'))
for i in range(n,0,-1):
    for j in range(1,i):
        print("  ",end="")
    for k in range(n,i-1,-1):
        print(i,end=" ")
    print(" ")