# For question go to:
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

no_of_queries = int(input())

itr = 0
while itr < no_of_queries:
    catA, catB, mouseC = map(int, input().split())
    
    if (abs(catA - mouseC)) > (abs(catB - mouseC)):
        print("Cat B")
    elif (abs(catA - mouseC)) < (abs(catB - mouseC)):
        print("Cat A")
    else:
        print("Mouse C")
    
    itr += 1