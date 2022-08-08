a=[2,3,5,1,4]

def findZigZagSequence(a, n):
    a.sort()
    #middle will be half length-1, as index starts from 0
    mid = int((n + 1)/2-1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    #
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        #
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

