#include<stdio.h>
int main()
{
    int a;
    printf("enter:");
    scanf("%d",&a);
    int *y = &a;
    printf("%u",&a);
    printf("%d",&a);
    printf("%u",&*y);
    printf("%d",&y);
    printf("%u",&y);
    printf("%d",&*y);
}