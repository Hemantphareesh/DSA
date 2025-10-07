class HelperFunctions:

    @staticmethod
    def swap(a, b):
        return b, a
    
class Sorting:
    def __init__(self, arr):
        self.helper = HelperFunctions()
        self.array = arr

    # Time: O(n²) | Space: O(1)
    def bubble_sort(self):
        '''
        Compare neighbors → if left is bigger than right, swap them.
        The biggest element moves to the end. then repeat.
        '''
        print("--------- Bubble Sort --------------")
        array = self.array[:]
        print(f"Before Sorting: {array}")
        n = len(array)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1): # Each iteration max element gets sorted to Exact possition so next itreation we can skip it
                if array[j]>array[j+1]:
                    array[j], array[j+1] = self.helper.swap(array[j], array[j+1])
                    swapped = True
            if not swapped:  # No swaps → array already sorted
                break
        print(f"after Sorting: {array}")
        return array

        




if __name__ == "__main__":
    array = [0,2,72,4,6,7,84,3,3,4,56,7,78,5,4,34,3,3,5,6,7,7,7,7,7]
    Sorting(array).bubble_sort()

