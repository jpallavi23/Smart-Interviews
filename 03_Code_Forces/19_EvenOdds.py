'''
Being a nonconformist, Volodya is displeased with the current state of things, particularly with the order of natural numbers (natural number is positive integer number). He is determined to rearrange them. But there are too many natural numbers, so Volodya decided to start with the first n. He writes down the following sequence of numbers: firstly all odd integers from 1 to n (in ascending order), then all even integers from 1 to n (also in ascending order). Help our hero to find out which number will stand at the position number k.
Input

The only line of input contains integers n and k (1 ≤ k ≤ n ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.
Output

Print the number that will stand at the position number k after Volodya's manipulations.

Examples
Input
10 3

Output
5

Input
7 7

Output
6

Note: In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}. The third place in the sequence is therefore occupied by the number 5.
'''

n, k_pos = map(int, input().split())
mark = k_pos - (n + 1) // 2
print([2*k_pos-1, 2*mark][mark>0])