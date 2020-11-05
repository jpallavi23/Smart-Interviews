'''
Print hollow rectangle pattern using '*'. See example for more details.

Input Format
Input contains two integers W and L. W - width of the rectangle, L - length of the rectangle.

Constraints
2 <= W <= 50 2 <= L <= 50

Output Format
For the given integers W and L, print the hollow rectangle pattern.

Sample Input 0
5 4

Sample Output 0
*****
*   *
*   *
*****
'''

cols, rows = map(int, input().split())

for itr in range(1, rows+1):
    for ctr in range(1, cols+1):
        if itr == 1 or itr == rows or ctr == 1 or ctr == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print("\r")