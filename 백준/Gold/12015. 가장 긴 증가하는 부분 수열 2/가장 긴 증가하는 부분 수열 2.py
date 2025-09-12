def bi_search(li,num):
    low=0
    high=len(li)
    while low<high:
        mid=(low+high)//2
        if li[mid]<num:
            low=mid+1
        else:
            high=mid
    return low
def f(li):
    temp=[]
    for i in range(len(li)):
        index=bi_search(temp,li[i])
        if index>=len(temp):
            temp.append(li[i])
            continue
        temp[index]=li[i]
    return len(temp)
input()
li=list(map(int,input().split(' ')))
print(f(li))