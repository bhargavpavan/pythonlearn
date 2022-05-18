#5 4 3 2 1
#  5 4 3 2
#    5 4 3
#      5 4
#        5
n = int(input('enter n value: '))
for i in range(1,n+1):
    for j in range(1,i):
        print("  ",end="")
    for k in range(n,i-1,-1):
        print(k,end=" ")
    print("\n")
