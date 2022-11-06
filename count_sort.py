a=[1,4,5,6,2]
n= len(a)
b= [0] * n
count= [0] *10

for i in range(n):
    count[a[i]]=count[a[i]]+1
    
for i in range(1,10):
    count[i]=count[i]+count[i-1]

i=n-1
while i>=0:
    b[count[a[i]]-1]=a[i]
    count[a[i]]-=1
    i=i-1
    
for i in range(n):
    a[i]=b[i]
    
print(a)
