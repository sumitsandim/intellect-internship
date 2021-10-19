num=int(input("enter no of rows you required:"))
for i in range(num):
    for j in range(num-i-1,-1,-1):
        print(j+1,end=' ')
    print()    
