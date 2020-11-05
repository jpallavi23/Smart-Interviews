# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-finding-missing-number

def findMissingNum(length_of_num_list, list_nums):
    total_sum = (length_of_num_list + 1) * (length_of_num_list + 2) / 2
    print(int(total_sum - sum(list_nums)))

if __name__ == '__main__':
    no_of_test_cases = int(input())
    iter = 1

    while iter <= no_of_test_cases:
        ar_count = int(input())
        ar = list(map(int, input().split()))
        findMissingNum(ar_count, ar)
        iter += 1