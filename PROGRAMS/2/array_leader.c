#include<stdio.h>

void print_array(int arr[], int size)
{
    int i;
    printf("[");
    for(i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
        if(i != size - 1) printf(", ");
    }
    printf("] \n");
}

void print_array_reverse(int arr[], int size)
{
    int i;
    printf("[");
    for(i = size-1; i > -1; i--)
    {
        printf("%d", arr[i]);
        if(i != 0) printf(", ");
    }
    printf("] \n");
}

//  Brute Force Method: Approach 1

void 
brute_force_array_leader(int arr[], int size)
{   int i, j, k = 0;
    int leader_array[size];
    for(i=0; i< size; i++)
    {
        int leader = 1;
        for(j=i+1; j< size; j++)
        {
            if(arr[j] > arr[i])
            {
                leader = 0;
                break;
            }
        }
        if(leader == 1)
        {
        leader_array[k++] = arr[i];
        }
    }
    print_array(leader_array, k);
} 

void 
array_leader(int arr[], int size)
{
    int i,j=0;
    int max_element = arr[size-1];
    int leader_array[size];
    for(i=size-1; i>-1; i--)
    {
        if(arr[i] >= max_element)
        {
            leader_array[j++] = arr[i];
            max_element = arr[i];
        }
    }
    print_array_reverse(leader_array, j);
}


int main()
{
    int arr[] = {16, 17, 4, 3, 5, 2};
    int size_of_array = sizeof(arr) / sizeof(arr[0]);
    printf("Array size: \n");
    print_array(arr, size_of_array);

    printf("Brute Force Array Leader: \n");
    brute_force_array_leader(arr, size_of_array);

    printf("Optimized Greedy Approach \n");
    array_leader(arr, size_of_array);



    return 0;

}