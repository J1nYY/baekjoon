#include <stdio.h>
int main(){
    short a,b;
    int c=0;
    scanf("%hd",&a);
    scanf("%hd",&b);
    printf("%d\n",a*(b%10));
    printf("%d\n",a*(b%100/10));
    printf("%d\n",a*(b/100));
    printf("%d\n",a*b);
}