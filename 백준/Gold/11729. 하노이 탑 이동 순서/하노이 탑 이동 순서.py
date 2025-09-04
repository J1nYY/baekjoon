def hanoi(n,st,de):
    if n==1:
        print(f"{st} {de}")
    elif n>1:
        other=(st+de)%3-3
        other=-other
        hanoi(n-1,st,other)
        print(f"{st} {de}")
        hanoi(n-1,other,de)
def hanoi_num(n):
    if n==1:
        return n
    elif n>1:
        return 2*hanoi_num(n-1)+1
num=int(input())
print(hanoi_num(num))
hanoi(num,1,3)