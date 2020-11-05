'''
After struggling and failing many times, Ujan decided to try to clean up his house again. He decided to get his strings in order first.

Ujan has two distinct strings s
and t of length n consisting of only of lowercase English characters. He wants to make them equal. Since Ujan is lazy, he will perform the following operation exactly once: he takes two positions i and j (1≤i,j≤n, the values i and j can be equal or different), and swaps the characters si and tj

. Can he succeed?

Note that he has to perform this operation exactly once. He has to perform this operation.
Input

The first line contains a single integer k
(1≤k≤10

), the number of test cases.

For each of the test cases, the first line contains a single integer n
(2≤n≤104), the length of the strings s and t

.

Each of the next two lines contains the strings s
and t, each having length exactly n

. The strings consist only of lowercase English letters. It is guaranteed that strings are different.
Output

For each test case, output "Yes" if Ujan can make the two strings equal and "No" otherwise.

You can print each letter in any case (upper or lower).

Example
Input
4
5
souse
houhe
3
cat
dog
2
aa
az
3
abc
bca

Output
Yes
No
No
No

Note: In the first test case, Ujan can swap characters s1
and t4, obtaining the word "house".

In the second test case, it is not possible to make the strings equal using exactly one swap of si
and tj.
'''

no_of_test_cases = int(input())
for test_cases in range(no_of_test_cases):
    length = int(input())
    s = input()
    t = input()
    check = [[x, y] for x, y in zip(s, t) if x != y]
    answer = len(check) == 0
    if len(check) == 2: answer = check[0] == check[1]
    print("Yes" if answer else "No")