# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-time-of-the-year

import datetime
import calendar
def class1():
    a=[]
    b=''
    timestamp=int(input())
    value=datetime.datetime.fromtimestamp(timestamp)
    myDate=value
    day=calendar.day_name[myDate.weekday()]
    a.append(value.strftime('%d-%m-%Y')+" "+day)
    for i in a:
        l=i.split('-')
        l[1]=calendar.month_name[int(l[1])]
        l[1]=l[1][0:3]
        l[1]=l[1].upper()
    for i in range(len(l)-1):
        b=b+str(l[i])+'-'
    b=b+l[len(l)-1]
    return b

if __name__ == "__main__":
    testcases=int(input())
    ap=[]
    for i in range(testcases):
        ap.append(class1())
    for i in range(testcases):
        print(ap[i])