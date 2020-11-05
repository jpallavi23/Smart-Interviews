# For question go to:
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

no_of_players = int(input())
leaderBoard_Scores = sorted(set(list(map(int, input().split()))), reverse = True)
no_of_games = int(input())
gameScores = list(map(int, input().split()))

length = len(leaderBoard_Scores)
for itr in gameScores:
    while (length > 0) and (itr >= leaderBoard_Scores[length - 1]):
        length -= 1
    print(length + 1)