'''
Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.

Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak - 1 also must be deleted from the sequence. That step brings ak points to the player.

Alex is a perfectionist, so he decided to get as many points as possible. Help him.
Input

The first line contains integer n (1 ≤ n ≤ 105) that shows how many numbers are in Alex's sequence.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105).
Output

Print a single integer — the maximum number of points that Alex can earn.

Examples
Input
2
1 2

Output
2

Input
3
1 2 3

Output
4

Input
9
1 2 1 3 2 2 2 2 3

Output
10

Note: Consider the third test example. At first step we need to choose any element equal to 2. After that step our sequence looks like this [2, 2, 2, 2]. Then we do 4 steps, on each step we choose any element equals to 2. In total we earn 10 points.
'''

size = int(input())
steps = input().split()
item = 0
while item < size:
    steps[item] = int(steps[item])
    item += 1
min_steps = min(steps)
max_steps = max(steps)
number_of_steps = [0]*(max_steps-min_steps+2)
item = 0
while item < size:
    number_of_steps[steps[item]-min_steps]+=1
    item += 1
item = 0
while item < (max_steps-min_steps+1):
    number_of_steps[item] = number_of_steps[item]*(item+min_steps)
    item += 1
check=[number_of_steps[0],max(number_of_steps[0],number_of_steps[1])]
item = 0
while item < (max_steps-min_steps-1):
    check+=[max(check[len(check)-1],check[len(check)-2]+number_of_steps[len(check)])]
    item += 1
print(check[-1])