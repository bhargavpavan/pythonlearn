#       1
#     1 2
#   1 2 3
# 1 2 3 4
n=int(input('enter n value:'))
for i in range(1,n+1):
    for j in range(i,n):
        print("  ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print(" ")
