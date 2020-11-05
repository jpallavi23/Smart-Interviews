# For question go to:
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

no_of_pieces = int(input())
nos_of_squares = list(map(int, input().split()))
birth_day, birth_month = list(map(int, input().split()))
count = 0

if birth_month <= no_of_pieces:
    sum_squares = 0
    ctr = 0
    while ctr < birth_month:
        sum_squares += nos_of_squares[ctr]
        ctr += 1
    
    if sum_squares == birth_day:
        count = 1
    else:
        count = 0
    
    itr = 0
    while ctr < no_of_pieces:
        sum_squares -= nos_of_squares[itr]
        sum_squares += nos_of_squares[ctr]
        
        count += 1 if sum_squares == birth_day else 0
        ctr += 1
        itr += 1

    print(count)