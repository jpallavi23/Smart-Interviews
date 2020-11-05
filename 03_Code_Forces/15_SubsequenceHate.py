for i in range(int(input())):
    sequence = input()
    no_of_ones, no_of_zeros = sequence.count('1'), sequence.count('0')
    ones, zeros = no_of_ones, no_of_zeros
    no_of_changes = []
    for i in range(len(sequence) - 1, -1, -1):
        no_of_changes.append(min(no_of_ones + zeros - no_of_zeros, no_of_zeros + ones - no_of_ones))
        if sequence[i] == '1':
            no_of_ones -= 1
        else:
            no_of_zeros -= 1
    print(min(no_of_changes))
