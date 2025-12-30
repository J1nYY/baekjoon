#include <stdio.h>
int main(){
    char a[1000000];
    int n=0;
    while(scanf("%s",&a)==1){
        n++;
    }
    printf("%d\n",n);
}