# For question go to:
# https://www.hackerrank.com/challenges/dynamic-array/problem

no_of_sequences, no_of_queries = map(int, input().split())

sequenceList = [[]] * no_of_sequences
lastAns = 0

for _ in range(no_of_queries):
    sequence = input().split(" ")
    ctr = (int(sequence[1]) ^ lastAns) % no_of_sequences

    if int(sequence[0]) == 1:
        sequenceList[ctr] = sequenceList[ctr] + [sequence[2]]
    else:
        num = int(sequence[2]) % len(sequenceList[ctr])
        lastAns = int(sequenceList[ctr][num])
        print(lastAns)