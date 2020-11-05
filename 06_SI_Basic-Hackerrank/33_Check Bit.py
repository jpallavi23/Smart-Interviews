'''
In a given integer - N, check whether the ith bit is set or not.

Input Format
Input contains integers - N and i.

Constraints
-1018 <= N <= 1018
0 <= i <= 63

Output Format
Print "true" if ith bit is set in the given integer N, "false" otherwise.

Sample Input 0
10 1

Sample Output 0
true
'''

number, bit = map(int, input().split())

if (number & (1 << bit)):
    print("true")
else:
    print("false")