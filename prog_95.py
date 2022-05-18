# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
        
n = int(input('enter n value: '))
for i in range(1,n+1):
    limit = 0
    for j in range(1,i):
        print("  ",end="")
    for k in range(1,n-i+2):
        print(k,end=" ")
        limit+=1
    print(" ")
