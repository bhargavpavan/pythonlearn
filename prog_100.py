#         5
#       5 4
#     5 4 3
#   5 4 3 2
# 5 4 3 2 1

n=int(input('enter n value:'))
k = 1
for i in range(n,0,-1):
    
    for j in range(1,i):
        print("  ",end="")
    for a in range(n,n-k,-1):
        print(a,end=" ")
    k+=1
    print(" ")
    
