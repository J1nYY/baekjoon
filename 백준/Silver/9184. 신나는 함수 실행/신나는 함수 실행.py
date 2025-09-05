list_d=[]
    
def f(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
            return 1
    elif a > 20 or b > 20 or c > 20:
            return f(20,20,20)
    if list_d[a][b][c] is None:
        if a < b and b < c:
            list_d[a][b][c]=f(a, b, c-1) + f(a, b-1, c-1) - f(a, b-1, c)
        else:
            list_d[a][b][c]=f(a-1, b, c) + f(a-1, b-1, c) + f(a-1, b, c-1) - f(a-1, b-1, c-1)
        
        return list_d[a][b][c]
        
    else:
        return list_d[a][b][c]
        
for i in range(0,21):
    list_j=[]
    for j in range(0,21):
        list_h=[]
        for h in range(0,21):
            list_h.append(None)
        list_j.append(list_h)
    list_d.append(list_j)
while True:
    a,b,c=map(int,input().split(' '))
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {f(a,b,c)}')