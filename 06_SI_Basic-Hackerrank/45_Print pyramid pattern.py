'''
Print pyramid pattern. See example for more details.

Input Format
First line of input contains a single integer N - the size of the pyramid.

Constraints
1 <= N <= 50

Output Format
For the given integer, print pyramid pattern.

Sample Input 0
5

Sample Output 0
    *
   ***
  *****
 *******
*********
'''

size = int(input())

for itr in range(1, size+1):
    temp = 0
    for ctr in range(1, (size - itr) + 1):
        print(end=" ")
    while temp != (2 * itr - 1):
        print("*", end="")
        temp += 1
    print("\r")