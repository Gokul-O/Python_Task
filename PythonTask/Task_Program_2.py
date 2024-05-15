rows=int(input("Enter the no of rows"))
num=1
for i in range(0,rows):
    for j in range(0,i+1):
        print(num,end=' ')
        num+=1
    print()

