'''
Print right-angled triangle pattern using palindrome strings. See example for more details.

Input Format
Input contains a integer N - lenght of the right angled triangle.

Constraints
1 <= N <= 26

Output Format
For the given integer N, print the right angled triangle.

Sample Input 0
5

Sample Output 0
A 
A B A 
A B C B A 
A B C D C B A 
A B C D E D C B A
'''

length_of_rtTri = int(input())

for itr in range(1, length_of_rtTri + 1):
    for ctr in range(1, itr + 1):
        print("{}".format(chr(ctr + 65 - 1)), end=" ")
    for ctr in range(itr - 1, 0, -1):
        print("{}".format(chr(ctr + 65 - 1)), end=" ")
    print("\r")