# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-check-power-of-two

def checkPower(check_num):
    if check_num == 0:
        return False
    while check_num != 1:
        check_num /= 2
        if check_num % 2 != 0 and check_num != 1:
            return False
    return True

if __name__ == '__main__':
    no_of_test_cases = int(input())
    iter = 1

    while iter <= no_of_test_cases:
        check_num = int(input())
        print(checkPower(check_num))
        iter += 1