list_a=[]


def f(num):
    
    if num==1:
        return 9
    else:
        for _ in range(10):
            i=[1]
            for _ in range(num):
                i.append(None)
            list_a.append(i)
        sum_num=0
        for i in range(num-2):
            for j in range(10):
                if j==0:
                    list_a[0][i+1]=list_a[1][i]
                elif j==9:
                    list_a[9][i+1]=list_a[8][i]
                else:
                    list_a[j][i+1]=list_a[j-1][i]+list_a[j+1][i]
        for j in range(2,9):
            sum_num+=list_a[j][num-2]
        sum_num*=2
        sum_num+=list_a[0][num-2]
        sum_num+=list_a[9][num-2]
        sum_num+=list_a[1][num-2]
    return sum_num%1000000000
num=int(input())
print(f(num))