'''
Print right-angled triangle pattern. See example for more details.

Input Format
First line of input contains a single integer N - the size of the triangle.

Constraints
1 <= N <= 50

Output Format
For the given integer, print the right-angled triangle pattern.

Sample Input 0
5

Sample Output 0
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''

number = int(input())

for itr in range(1, number+1):
    difference = number - 1
    jtr = itr
    for ctr in range(1, itr+1):
        print(jtr, end=" ")
        jtr += difference
        difference -= 1
    print("\r")