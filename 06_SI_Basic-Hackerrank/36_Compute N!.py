'''
Given a non-negative number - N. Print N!

Input Format
Input contains a number - N.

Constraints
0 <= N <= 10

Output Format
Print Factorial of N.

Sample Input 0
5

Sample Output 0
120
'''

number = int(input())
factorial = 1

if number < 0:
    print("0")
else:
    for itr in range(1, number+1):
        factorial = factorial * itr
    print(factorial)