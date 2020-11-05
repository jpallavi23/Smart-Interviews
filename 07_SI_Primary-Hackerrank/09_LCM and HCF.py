# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-lcm-and-hcf

def hcf(a, b):
   while(b):
       a, b = b, a % b
   return a

def lcm(a, b):
    ans = (a * b) // hcf(a, b)
    return ans

if __name__ == "__main__":
    no_of_test_cases = int(input())
    while(no_of_test_cases > 0):
        num1, num2 = map(int, input().split())
        print("{} {}".format(lcm(num1, num2), hcf(num1, num2)))
        
        no_of_test_cases -= 1