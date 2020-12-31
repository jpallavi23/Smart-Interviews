# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-tower-of-hanoi

def TowerOfHanoi(size, src, temp, dest):
    if size == 1:
        print("Move 1 from {} to {}".format(src, dest))
        return
    TowerOfHanoi(size - 1, src, dest, temp)
    print("Move {} from {} to {}".format(size, src, dest))
    TowerOfHanoi(size - 1, temp, src, dest)
    
if __name__ == "__main__":
    no_of_testcases = int(input())
    while no_of_testcases > 0:
        no_of_disks = int(input())
        print((2**no_of_disks) - 1)
        TowerOfHanoi(no_of_disks, 'A', 'B', 'C')
        no_of_testcases -= 1