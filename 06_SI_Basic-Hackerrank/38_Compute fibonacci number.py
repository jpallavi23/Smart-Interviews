'''
For a given positive integer - N. Compute Nth fibonacci number.

Input Format
Input contains a positive integer - N.

Constraints
1 <= N <= 20

Output Format
For given input, print the Nth fibonacci number.

Sample Input 0
4

Sample Output 0
3

Explanation 0
    The fibonacci series:
    1, 1, 2, 3, 5, 8,......
    At 4th position we have 3.
'''

number = int(input())

first, second = 1, 1
next_num = 1

if number == 0 or number == 1:
    print(number)
else:
    for itr in range(2, number):
        next_num = first + second
        first = second
        second = next_num
    print(next_num)