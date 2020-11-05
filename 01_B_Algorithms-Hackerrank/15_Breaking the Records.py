# For question go to:
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

no_of_games = int(input())
scores = list(map(int, input().split()))

highScore = scores[0]
lowScore = scores[0]
bestHighestScore_count = 0
worstLowestScore_count = 0

# print(highScore, lowScore, bestHighestScore_count, worstLowestScore_count)
# print("\n")

for score in scores:
    if score > highScore:
        bestHighestScore_count += 1
        highScore = score
        # print(score, bestHighestScore_count)
    elif score == highScore or score == lowScore:
        # print(score)
        continue
    elif score < lowScore:
        worstLowestScore_count += 1
        lowScore = score
        # print(score, worstLowestScore_count)

# print("\n")
print(bestHighestScore_count, worstLowestScore_count)