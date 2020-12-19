# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-overlapping-rectangles

def overlappingRectangles(x_bl1, y_bl1, x_tr1, y_tr1, x_bl2, y_bl2, x_tr2, y_tr2):
    area1 = abs(x_bl1 - x_tr1) * abs(y_bl1 - y_tr1)
    area2 = abs(x_bl2 - x_tr2) * abs(y_bl2 - y_tr2)
    x_dist = (min(x_tr1, x_tr2) - max(x_bl1, x_bl2))
    y_dist = (min(y_tr1, y_tr2) - max(y_bl1, y_bl2))
    
    area = 0
    if x_dist > 0 and y_dist > 0:
        area = x_dist * y_dist
    
    return (area1 + area2 - area)
    
if __name__ == "__main__":
    no_of_testcases = int(input())
    while no_of_testcases > 0:
        x_bl1, y_bl1, x_tr1, y_tr1 = map(int, input().split())
        x_bl2, y_bl2, x_tr2, y_tr2 = map(int, input().split())
        print(overlappingRectangles(x_bl1, y_bl1, x_tr1, y_tr1, x_bl2, y_bl2, x_tr2, y_tr2))
        no_of_testcases -= 1