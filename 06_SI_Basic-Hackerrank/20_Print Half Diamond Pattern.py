'''
Print half diamond pattern using '*'. See example for more details.

Input Format
Input contains a single integer N.

Constraints
1 <= N <= 50

Output Format
For the given integer, print the half diamond pattern.

Sample Input 0
3

Sample Output 0
*
**
***
**
*
'''

size = int(input())
temp = size
for _ in range(1, size*2):
    if _ >= size:
        print("*"*temp)
        temp -= 1
    else:
        print("*"*_)