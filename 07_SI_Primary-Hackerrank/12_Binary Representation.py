# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-binary-representation

def decToBin(dec_num):
    if dec_num > 1:
        decToBin(dec_num // 2)
    print(dec_num % 2, end='')

if __name__ == '__main__':
    no_of_test_cases = int(input())
    iter = 1

    while iter <= no_of_test_cases:
        dec_num = int(input())
        decToBin(dec_num)
        print()
        iter += 1