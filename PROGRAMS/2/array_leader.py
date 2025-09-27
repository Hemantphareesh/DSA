arr = [16, 17, 4, 3, 5, 2]

"""
 Brute Force Method: 
"""

def array_leader_brute_force(arr: list):
    leader_array = []
    for i in range(len(arr)):
        found_leader = True
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                found_leader = False
                break
        if found_leader:
            leader_array.append(arr[i])
    return leader_array


array_leader_brute_force(arr=arr)

"""
Greedy Algorithm
"""

def array_leader(arr: list):
    leader_array = []
    max_element = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= max_element:
            max_element = arr[i]
            leader_array.append(max_element)
    leader_array.reverse() 
    return leader_array


array_leader(arr=arr)