# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-trailing-zeros

def trailingZeros(number):
    count = 0
    itr = 5
    while(number / itr >= 1):
        count += int(number / itr)
        itr *= 5
    return int(count)
    
if __name__ == "__main__":
    no_of_testcases = int(input())
    while no_of_testcases > 0:
        number = int(input())
        print(trailingZeros(number))
        no_of_testcases -= 1