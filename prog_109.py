#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4
n = int(input('enter n value: '))

a=0
count = 0
count1 = 0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("  ",end="")
        count+=1
    
    while(a!=((2*i)-1)):
        if count <= n-1:
            print(i+a,end=" ")
            count+=1
        else:
            count1+=1
            print(i+a-(2*count1),end=" ")
        a+=1
    count1 = count = a = 0
    print()

    