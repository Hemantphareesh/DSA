# DSA
Data Structures & Algorithms (DSA)

Compile:
```
gcc <file>.c -o <file>
Python3 <file>.py
```

1. Pattern Programs

2. Array Leaders: You are given an array arr of positive integers. Your task is to find all the leaders in the array. 
   An element is considered a leader if it is greater than or equal to all elements to its right. 
   The rightmost element is always a leader.
    - Examples:
        Input: arr = [16, 17, 4, 3, 5, 2]
        Output: [17, 5, 2]
        Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
   
   ***Approach:***
   Approach 1: Brute Force
   Every value have to be checked if its right side is greater than itself.
   for that we require 2 loops, first loop will be keep track of current value with range of (0, len(arr)), lets say i is defined.
   arr[i] will be current element. as default we will consider arr[i] will be leader, that is leader flag will be set to arr[i], then we have to iterate through out the loop to check if any other element is greater than arr[i], for that we will use another loop to iterate to rest of the elements, lets say j,  but here in j we dont need to check the currentelement that is arr[i] so we have to iterate from i+1 to len(arr). in j loop we will set flag leader as true if any element is greater than arr[i], and break out of loop. if no greater found we will print that current value. 

   Here the problem is Outer Loop takes O(n) times and inner loop takes O(n+1) time. that gives O(n^2) so lets try an approch which will reduce complexity.

   Approach 2: Greedy Algorithm
   scan from right to left assuming the element is greater than past item, we will consider right most elemet will always be a leader.
   so for iterating from right to left consider a variable max_element which is assumed to be a leader and while moving left if any element is greater than max_element then that value is set to be a leader.
   for looping lets use range(len(arr), -1, -1) where -1 for reverse and in c we will use decrement operations. 
   Code Complexity is O(n) which is way less than earlier.

   what exactly is Greedy Algorithm: is a problem-solving approach where you build the solution step by step, always choosing the best (locally optimal) option at the current step, with the hope that this will lead to the global optimum.
   For a greedy algorithm to work, the problem must have two properties:
   1. Greedy Choice Property : A global solution can be built by choosing local optimums.
   2. Optimal Substructure: The problem can be broken into smaller subproblems that can be solved independently.

   Application Usages in case of IoT:
   1. Signal Processing:  In sensor data streams (like temperature, voltage, IoT signals), leaders identify local dominance points where the value is stronger than anything after it. Useful for fault detection (e.g., sudden spikes). 
   2. Data Compression / Optimization: Leaders can represent a minimal subset of data that still carries the "dominance" property. Instead of storing all numbers, we keep only the leaders (reducing memory in certain analytics pipelines).
   3. Useful for forecasting, optimization, trend analysis, and decision-making.

3. Sort 0s, 1s and 2s: 
    Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
    Note: You need to solve this problem without utilizing the built-in sort function.

    Examples:
    Input: arr[] = [0, 1, 2, 0, 1, 2]
    Output: [0, 0, 1, 1, 2, 2]
    Explanation: 0s, 1s and 2s are segregated into ascending order.

    Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    Explanation: 0s, 1s and 2s are segregated into ascending order.

    Follow up: Could you come up with a one-pass algorithm using only constant extra space?

    ***Approach:***
    Approach 1: Brute Force
    given an array sort the array with out use of inbuild functions.
    In python lets create a dictionary hash map method to sort each with 0, 1 and 2. then start priting from greater to lower values.
    second way is use Counting Method for loop to iterate though each, and keep track of it in 3 variables, 
