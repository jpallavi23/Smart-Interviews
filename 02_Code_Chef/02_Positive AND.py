# For question go to:
# https://www.codechef.com/OCT20B/problems/POSAND


def powerOfTwo(number):
    return number != 0 and ((number & (number - 1)) == 0)


no_of_test_cases = int(input())

while(no_of_test_cases > 0):
    number = int(input())
    if number == 1:
        print("1", end = "")
    elif number == 3:
        print("1 3 2", end = "")
    elif number == 5:
        print("2 3 1 5 4", end = "")
    elif powerOfTwo(number):
        print("-1", end = "")
    else:
        print("2 3 1 5 4 ")
        ctr = 6
        while(ctr <= number):
            if powerOfTwo(ctr):
                print("{} {}".format(ctr + 1, ctr))
                ctr += 2
            else:
                print(ctr)
                ctr += 1
        print(end=" ")
    print()
    no_of_test_cases -= 1