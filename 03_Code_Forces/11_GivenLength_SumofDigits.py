'''
You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.
Input

The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.
Output

In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).

Examples
Input
2 15

Output
69 96

Input
3 0

Output
-1 -1
'''

m, s = map(int, input().split())
minimum = m*[0]
maximum = m*[0]
minimum[0] = 1

for num in range(1, s):
    for value in range(1, m+1):
        if minimum[-value] != 9: minimum[-value] += 1; break
        
for num in range(s):
    for value in range(0, m):
        if maximum[value] != 9: maximum[value] += 1; break

if (m,s) == (1, 0): print(0, 0); exit(0)

if sum(minimum) ==  s and sum(maximum) == s:
    for num in minimum: 
        print(num, end = '')
    print(" ", end = '')
    for num in maximum: 
        print(num, end = '')
else:
    print("-1 -1")