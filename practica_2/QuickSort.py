#QuickSort
def intercabiar(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp

def Particionar(A,p,r):
    x=A[p] 
    i=p 
    for j in range(p+1,r+1): 
        if (A[j]>=x): 
            i=i+1           
            intercabiar(A,i,j) 
    intercabiar(A,i,p)
    return i

def Quicksort(A,p,r):
    if(p<r):
        q=Particionar(A,p,r)
        print(A[p:r])
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)

A=[0,2,8,7,1,3,5,6,4]
print(A)
Quicksort(A,1,len(A)-1)
print(A)

