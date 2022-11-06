a=[1,4,5,6,2]
n=len(a)
for i in range(1,n):
    temp=a[i]
    j=i-1
    while( (j>=0) & (a[j]>temp)):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
    
    
print(a)
