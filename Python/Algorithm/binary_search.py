# Uses python3
import sys

def binary_search(a, x):
    return xxx(a,x,0,len(a)-1)

def xxx(a,x,i,j):
    mid = int((i+j)/2)
    if i>j:
        return -1
    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return xxx(a,x,i,mid-1)
    elif x>a[mid]:
        return xxx(a,x,mid+1,j)



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
