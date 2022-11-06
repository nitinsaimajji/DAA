a=[1,4,5,6,2]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
      
        
        
        
print(a)        
