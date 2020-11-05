# For question go to:
# https://www.hackerrank.com/challenges/sparse-arrays/problem#!

strings_size = int(input())
strings = []
for _ in range(strings_size):
    strings.append(input())

queries_size = int(input())
queries = []
for _ in range(queries_size):
    queries.append(input())

for itr in queries:
    result = 0
    for ctr in strings:
        if itr == ctr:
            result += 1
    
    print(result)