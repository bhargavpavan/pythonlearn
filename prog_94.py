# 11111
#  2222
#   333
#    44
#     5
n=int(input("enter n value:"))
for i in range(1,n+1):
    for k in range(0,i):
        print("  ",end="")      
    for j in range(1,n-i+1):
        print(i,end=' ')
    print(" ")pwd

