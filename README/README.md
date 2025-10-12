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

   **_Approach:_**
   Approach 1: Brute Force
   Every value have to be checked if its right side is greater than itself.
   for that we require 2 loops, first loop will be keep track of current value with range of (0, len(arr)), lets say i is defined.
   arr[i] will be current element. as default we will consider arr[i] will be leader, that is leader flag will be set to arr[i], then we have to iterate through out the loop to check if any other element is greater than arr[i], for that we will use another loop to iterate to rest of the elements, lets say j, but here in j we dont need to check the currentelement that is arr[i] so we have to iterate from i+1 to len(arr). in j loop we will set flag leader as true if any element is greater than arr[i], and break out of loop. if no greater found we will print that current value.

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

   1. Signal Processing: In sensor data streams (like temperature, voltage, IoT signals), leaders identify local dominance points where the value is stronger than anything after it. Useful for fault detection (e.g., sudden spikes).
   2. Data Compression / Optimization: Leaders can represent a minimal subset of data that still carries the "dominance" property. Instead of storing all numbers, we keep only the leaders (reducing memory in certain analytics pipelines).
   3. Useful for forecasting, optimization, trend analysis, and decision-making.

3. Contains Duplicate: Given an integer array nums, return true if any value appears at least twice in the array,
   and return false if every element is distinct.
   Input: nums = [1,2,3,1]

   Python:
   Approach 1:
   we require 2 loops one for iteration and other for scanning all the elements to right of it.
   first for loop i in range(0, len(nums)) and second loop to iterate through right side to check j in range(i+1, len(nums))
   this approch failed because compleixity is very high so need to find optimal problem solution. since approch one give O(n^2) Complexity.

   Approach 2:
   before finding duplicates we need to sort the element, now sorting we use inbuild .sort() and compare nearby values and if same then duplicate is there.
   thia approch is very good if inbuild libraries are supported but our problem is in no interviews or no places we can use libraries so we need to build from scratch.

   Approach 3:
   Lets do a hybrid approach for this, combination of both InsertionSort and HeapSort
   if array size is < 50 we will use InsertionSort which is O(n^2)
   for rest use HeapSort which is O(n log n). best for large arrays with memory constraints.

   if array size is < 255 we will use Counting/Radix which is O(n), only integers.
   to understand this lets first understand tradeoff which we have to give in exchage of speed and Stability.
   Sorting algorithms:
   MergeSort: Time Complexity -> O(n log n), Space Complexity -> O(n), preserves order. Fast, but extra memory may slow it down.
   HeapSort: Time Complexity -> O(n log n), Space Complexity -> O(1), change order, Slightly slower than MergeSort.

   now question will be there why HeapSort if stability issue is there? so when i said stability is there it does not mean sorting will change, data will be sorted perfectly, stability problem only matters if the order of duplicates is important in your application. that means it matters if array is having key value pairs then if osrting is based on value then key may get swapped but it will still be sorted.

   after this lets understand what is TimSort which is pretty intresting and will be fun implementing it to find out how python, java uses timsort in their inbuild sorting functions.

   Lets understand sorting more deeply :

   InsertionSort:
   Small arrays (≤ 32–50 elements)| All Data types| Stable| Time: O(n²)| Space: O(1)| Very fast for tiny arrays; used inside TimSort for short runs.

   QuickSort:
   Medium arrays (50 – ~10k)| All Data types| Not stable| Time: O(n²)| Space: O(log n)| Fastest in practice; in-place; pivot choice avoids worst-case.| Embedded systems often prefer QuickSort for medium to large arrays.

   MergeSort:
   Large arrays, stability needed| All Data types| Stable| Space: O(n log n)| Space: O(n)| Cache-friendly, predictable, used in external sorting (disk-based).

   HeapSort:
   Large arrays, low memory (in-place O(1))| All Data types| Not stable| O(n log n)| O(1)| Slower than QuickSort/MergeSort because of cache-unfriendly access.

   CountingSort:
   Small integer range (0–k), e.g. 0–255| Integers only| Stable| O(n + k)| O(k)| Extremely fast; good for byte/char data.| Used in networking, embedded logs, byte/packet processing.

   RadixSort:
   Larger integers/strings (multi-digit)| Integers, strings| Stable| O(n·d) (d = digits)| O(n + k)| Uses CountingSort as subroutine; great for large int ranges.| Used in networking, embedded logs, byte/packet processing.

   TimSort:
   Real-world, mixed data| All types| Stable| O(n log n) worst, O(n) best| O(n)| Hybrid of Insertion + Merge; optimizes for partially sorted data.

   BubbleSort / SelectionSort: No Pratical application. skipping.

4. Move Zeroes
   Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
   Note that you must do this in-place without making a copy of the array.

   Example 1:
   Input: nums = [0,1,0,3,12]
   Output: [1,3,12,0,0]

   Example 2:
   Input: nums = [0]
   Output: [0]

   Approch: Use 2 pointer pattern approch.
   Whenever I find a value that belongs in the front, I place it at position and then move position forward.


