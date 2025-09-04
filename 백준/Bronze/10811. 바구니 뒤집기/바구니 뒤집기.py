def reverse(array,n,v):
    temp=array[n-1:v]
    temp.reverse()
    array[n-1:v]=temp
init=list(map(int,input().split(' ')))
array=[]
for i in range(1,init[0]+1):
    array.append(i)
for i in range(init[1]):
    num=list(map(int,input().split(' ')))
    reverse(array,num[0],num[1])
for i in array:
    print(i,end=' ')