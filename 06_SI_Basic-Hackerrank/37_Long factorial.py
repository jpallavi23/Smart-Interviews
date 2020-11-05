'''
Given Number N. Print N!

Input Format
The input contains a number - N.

Constraints
0 <= N <= 20

Output Format
Print factorial of N.

Sample Input 0
3

Sample Output 0
6
'''

number = int(input())
factorial = 1

if number < 0:
    print("0")
else:
    for itr in range(1, number+1):
        factorial = factorial * itr
    print(factorial)