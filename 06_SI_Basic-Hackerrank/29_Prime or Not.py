'''
Given a positive integer - N. Check whether the number is prime or not.

Input Format
Input contains positive integer - N.

Constraints
1 <= N <= 109

Output Format
Print "Yes" if the number is prime, "No" otherwise.

Sample Input 0
11

Sample Output 0
Yes
'''

number = int(input())

if number <= 1:
    print("No")
    exit(0)
else:
    for i in range(2,number//2):
        if number % i == 0:
            print("No")
            break
        else:
            print("Yes")
            quit()