n=input("jumian=")
n=int (n)
m=0
jumian=[]
for i in range(8*n):
    jumian.append(input())
for i in range(1,(n+1)):
    m=0
    for j in range(1,(i+1)):
        if jumian[8*(i-1):8*i]==jumian[8*(j-1):8*j]:
            m=m+1
    print(m) 