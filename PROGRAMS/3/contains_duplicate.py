class Sort:
    def __init__(self, nums):
        self.array = nums
        self.size = len(self.array)
    
    # Insertion Sort | Ascending order | upto 30 elements | Time: O(n²)| Space: O(1)

    def insertion_sort(self):
        arr = self.array[:]
        for i in range(1, self.size):
            current_value = arr[i]
            j=i-1
            while(j>=0 and arr[j]>current_value):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = current_value
        return arr
    
    # Quick Sort | Ascending order | Upto 50 – ~10k Elements | Time: O(n²)| Space: O(log n)

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

    def partition(self, arr,start, end):
        pivot = arr[end]
        boundary = start - 1
        for i in range(start, end):
            if arr[i] <= pivot: # if it is smaller than pivot increase boundary and then swap
                boundary+=1
                self.swap(arr, i, boundary)
        self.swap(arr, boundary + 1, end)
        return boundary + 1    

    def q_sort(self, arr, start, end):
        if start < end:
            boundary = self.partition(arr, start, end)
            self.q_sort(arr, start, boundary - 1)
            self.q_sort(arr, boundary + 1, end)
    
    def quick_sort(self):
        arr = self.array[:]
        self.q_sort(arr, 0, len(arr) - 1)
        return arr   
    
    # Bubble Sort | Ascending order | Not Used Anywhere | Time: O(n²)| Space: O(1) | Swapping is more expensive than just shifting values in memory.

    def bubble_sort(self):
        arr = self.array[:]
        for i in range(0 , len(arr)):
            is_sorted = True
            for j in range(1, len(arr)-i):
                if arr[j-1] > arr[j]:
                    self.swap(arr, j-1, j)
                    is_sorted = False
            if is_sorted:
                return arr
        return arr

    def selection_sort(self):
        arr = self.array[:]
        for i in range(0, len(arr)):
            min_index = i
            for j in range(i, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            self.swap(arr, min_index, i)
        return arr
    
    # Merge Sort | Divide and Conquer | Time: O(n logn)| Space: O(n)

    def merge_sort(self):
        pass


class Duplicated:
    def __init__(self, nums):
        self.array = nums
        self.size = len(self.array)

    def contains_duplicate_approach1(self):
        arr = self.array[:]
        for i in range(0, self.size):
            for j in range(i+1, self.size):
                if arr[j] == arr[i]:
                    return True
        return False
    
    def contains_duplicate_approach2(self):
        numbers = self.array[:]
        numbers.sort()
        for i in range(self.size -1):
            if numbers[i] == numbers[i+1]:
                return True
        return False
    

if __name__ == "__main__":
    nums =  [8,2,4,5,7,8,9,96,5,4,3,3,3,3,6]
    duplicate = Duplicated(nums)
    print(duplicate.contains_duplicate_approach1())
    print(duplicate.contains_duplicate_approach2())
    sorts = Sort(nums)
    print(sorts.insertion_sort())
    print(sorts.quick_sort())
    print(sorts.bubble_sort())
    print(sorts.selection_sort())