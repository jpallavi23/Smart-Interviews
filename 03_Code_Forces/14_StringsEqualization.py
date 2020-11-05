'''
You are given two strings of equal length s and t

consisting of lowercase Latin letters. You may perform any number (possibly, zero) operations on these strings.

During each operation you choose two adjacent characters in any string and assign the value of the first character to the value of the second or vice versa.

For example, if s

is "acbc" you can get the following strings in one operation:

    "aabc" (if you perform s2=s1

);
"ccbc" (if you perform s1=s2
);
"accc" (if you perform s3=s2
or s3=s4
);
"abbc" (if you perform s2=s3
);
"acbb" (if you perform s4=s3

    ); 

Note that you can also apply this operation to the string t

.

Please determine whether it is possible to transform s
into t

, applying the operation above any number of times.

Note that you have to answer q

independent queries.
Input

The first line contains one integer q
(1≤q≤100

) — the number of queries. Each query is represented by two consecutive lines.

The first line of each query contains the string s
(1≤|s|≤100

) consisting of lowercase Latin letters.

The second line of each query contains the string t
(1≤|t|≤100, |t|=|s|

) consisting of lowercase Latin letters.
Output

For each query, print "YES" if it is possible to make s
equal to t

, and "NO" otherwise.

You may print every letter in any case you want (so, for example, the strings "yEs", "yes", "Yes", and "YES" will all be recognized as positive answer).

Example
Input
3
xabb
aabx
technocup
technocup
a
z

Output
YES
YES
NO

Note: In the first query, you can perform two operations s1=s2
(after it s turns into "aabb") and t4=t3 (after it t turns into "aabb").

In the second query, the strings are equal initially, so the answer is "YES".

In the third query, you can not make strings s
and t equal. Therefore, the answer is "NO".
'''

no_of_test_cases = int(input())
for test_cases in range(no_of_test_cases):
    s = sorted(input().lower())
    t = sorted(input().lower())
    print('NO' if len((set(s)) & set(t)) == 0 else 'YES')