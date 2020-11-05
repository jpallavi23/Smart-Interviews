# For question go to:
# https://www.hackerrank.com/challenges/drawing-book/problem

no_of_pages = int(input())
page_reqd = int(input())

min_no_of_turns = (no_of_pages // 2) - (page_reqd // 2)
if min_no_of_turns > (page_reqd // 2):
    min_no_of_turns = page_reqd // 2

print(min_no_of_turns)