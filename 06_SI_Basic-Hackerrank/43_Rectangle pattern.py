'''
Print rectangle pattern. See example for more details.

Input Format
First line of input contains a single integer N - the size of the rectangle.

Constraints
1 <= N <= 50

Output Format
For the given integer, print rectangle pattern.

Sample Input 0
5

Sample Output 0
5432*
543*1
54*21
5*321
*4321
'''

size_of_rectangle = int(input())

for itr in range(1, size_of_rectangle+1):
    for ctr in range(1, size_of_rectangle+1):
        if ctr == size_of_rectangle - itr + 1:
            print("*",end="")
        else:
            print(size_of_rectangle-ctr+1,end="")
    print("\r")