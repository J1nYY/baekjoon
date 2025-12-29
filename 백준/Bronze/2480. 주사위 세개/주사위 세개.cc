#include <stdio.h>
#define max(x, y) ((x) > (y) ? (x) : (y))
int main(){
    short a,b,c;
    scanf("%hd %hd %hd",&a,&b,&c);
    if(a!=b&&b!=c&&c!=a){
        printf("%d", max(max(a,b),c)*100);
    }
    else if (a==b&&b==c)
    {
        printf("%d",a*1000+10000);
    }
    else if(b==c){
        printf("%d",b*100+1000);
    }
    else
    {
        printf("%d",a*100+1000);
    }
    
}