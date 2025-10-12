#include<stdio.h>

int main()
{
    int nums[6] = {3, 1, 2, 4, 5, 6};
    int index;
    int num_size = sizeof(nums)/sizeof(nums[0]);
    int position = 0;
    for(index = 0; index<num_size; index++ )
    {
        if(nums[index]%2 == 0)
        {
            if(position != index)
            {
                int temp = nums[position];
                nums[position] = nums[index];
                nums[index] = temp;
            }
            position +=1;
        }
    }

    for(index = 0; index<num_size; index++ )
    {
        printf("%d ", nums[index]);
    }

}