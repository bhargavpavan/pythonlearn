# 1 1 1 1 1
#   2 2 2 2
#     3 3 3
#       4 4
#         5
n=int(input("enter n value:"))
for i in range(1,n+1):
    for k in range(1,i):
        print("  ",end="")      
    for j in range(0,n-i+1):
        print(i,end=' ')
    print(" ")

