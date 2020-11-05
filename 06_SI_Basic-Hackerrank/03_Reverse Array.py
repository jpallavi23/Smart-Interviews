'''
Print array in reverse order.
Note: Try solving this using recursion. Do not use any inbuilt functions/libraries for your main logic.

Inpt Format

First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints
1 <= N <= 100
0 <= ar[i] <= 1018

Output Format
Print array in reverse order.

Sample Input 0
5
2 19 8 15 4

Sample Output 0
4 15 8 19 2
'''
size = int(input())
array = list(map(int, input().split()))
reverse = array[::-1]

print(*reverse)