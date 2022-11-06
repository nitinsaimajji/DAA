a=[154,564,56,5,45,25]
n=len(a)
flag=0
for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp


print(a)

