def fibonacci(n,count):
    f=[]
    f.append(1)
    f.append(1)
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
        count['fibonacci']+=1
    print(f"{f[len(f)-1]} {count['fibonacci']}")
count={'fibonacci':0}
num=int(input())
fibonacci(num,count)