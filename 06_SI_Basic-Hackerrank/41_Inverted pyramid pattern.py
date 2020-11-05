'''
Print hollow half inverted pyramid pattern. See example for more details.

Input Format
First line of input contains a single integer N - the size of the pyramid.

Constraints
1 <= N <= 50

Output Format
For the given integer, print hollow half inverted pyramid pattern.

Sample Input 0
5

Sample Output 0
* * * * *
*     *
*   *
* *
*
'''

size = int(input())

for itr in range(1, size+1):
    for ctr in range(1, size+1):
        if itr == 1 or ctr == 1 or ctr == size - itr + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\r")