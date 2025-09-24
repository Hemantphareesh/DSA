#include<stdio.h>

void 
pattern1()
{
    int i, j;
    for(i = 0; i < 5; i++)
    {
        for(j = 5; j > i; j--)
        {
            printf("%d ", j);
        }
        printf("\n");
    }
}
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
'''



int main()
{
    pattern1();
    
}