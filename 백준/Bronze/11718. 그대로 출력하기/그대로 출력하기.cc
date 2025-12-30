#include <stdio.h>

int main(){
    char a[100];
    int size;
    while(size=fread(a,sizeof(char),100,stdin))
        fwrite(a,sizeof(char),size,stdout);
}