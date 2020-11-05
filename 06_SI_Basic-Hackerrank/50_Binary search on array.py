'''
Implement binary search. Given a sorted array, search key in the array. If key not found print "false", otherwise print "true".

Input Format
First line of input contains two integers N and K. N is the size of array and K is the key. Second line contains array elements.

Constraints
1 <= N <= 102
0 <= ar[i] <= 109

Output Format
Print "true" if key is present in the array. Otherwise, print false.

Sample Input 0
5 19
2 19 23 35 38

Sample Output 0
true
'''

def binarySearch(array_elements, size_of_array, search_key):
    start = 0
    end = size_of_array - 1
    middle = 0

    while start <= end:
        middle = (end + start) // 2
        if array_elements[middle] < search_key:
            start = middle + 1
        elif array_elements[middle] > search_key:
            end = middle - 1
        else:
            return middle
    return -1

if __name__ == "__main__":
    size_of_array, search_key = map(int, input().split())
    array_elements = list(map(int, input().split()))

    result = binarySearch(array_elements, size_of_array, search_key)

    if result == -1:
        print("false")
    else:
        print("true")