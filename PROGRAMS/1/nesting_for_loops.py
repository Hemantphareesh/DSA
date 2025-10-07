"""
Outer loop → Rows
Inner loop → Columns
Outer loop runs n times.
Inner loop runs m times for each outer loop.
Total = n x m.
nested loops often mean O(n²) in complexity.

Outer loop → how many times you “repeat a line”.
Inner loop → what is printed per line.
"""
# pattern 1

def pattern1():
    for i in range(0, 5):
        for j in range (5, i, -1):
            print(j, end=' ')
        print()
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
'''

# pattern 2
def pattern2():
    '''
    rows => 5
    columes => 5,4,3,2,1
    value = increase by 1
    '''
    var = 'A'
    value = ord(var)
    for i in range(5, 0, -1):
        for j in range(i):
            print(chr(j + value), end=' ')
        print()
'''
A B C D E 
A B C D 
A B C 
A B 
A 
'''

def pattern3():
    array = [1,2,3,8,8,9,0,0,0,9,8,6,5,43,3,2,2,1,1,1,1,1]
    for i in range(0, len(array)):
        for j in range(1, len(array)):
            print(f"j: {array[j]}, j-1: {array[j-1]}")

if __name__ == "__main__":
    pattern1() 
    pattern2()
    pattern3()
