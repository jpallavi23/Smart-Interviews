# For question go to"
# https://www.codechef.com/OCT20B/problems/CVDRUN

no_of_test_cases = int(input())
while no_of_test_cases:
    no_of_test_cases -= 1
    no_of_cities, size_jumps, currCity, myCity = [int(itr) for itr in input().split()]
    effectCount = [0] * no_of_cities
    while True:
        if effectCount[currCity]:
            flag = 1
            break
        effectCount[currCity] +=1
        currCity = (currCity + size_jumps) % no_of_cities
        if effectCount[myCity]:
            flag = 2
            break
    if size_jumps == 0 or size_jumps == no_of_cities:
        if currCity == myCity:
            print("YES")
        else:
            print("NO")
    elif flag==2:
        print("YES")
    else:
        print("NO")