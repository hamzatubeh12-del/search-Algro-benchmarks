import random 
import time 


def linear_search(M, value):
    for i , row in enumerate(M):
        for j, element in enumerate(row):
            if element == value:
                return [i, j]
    return [-1, -1]

def BiSearch (row,value):
    lo=0 
    hi=len(row)-1
    while lo <=hi:
        mid = (lo+hi)//2
        if row[mid ] > value:
            hi=mid-1
        elif row[mid] < value:
            lo=mid+1
        else:
            return mid
    return -1
def row_BiSearch(M , value):
    #Binary serach in every row 
    for i , row in enumerate(M):
        j=BiSearch(row,value)
        if j != -1 :
            return [i,j]
    return [-1,-1]

def staircase_search(M,value):
    # we start at top right then see if it bigger then vlaue we go left 
    #                               , if smaller we go down 
    if not M or not M[0]:
        return [-1,-1]
    r, c =0, len(M[0])-1
    while r< len(M) and c>= 0 :
        v= M[r][c]
        if v == value :
            return [r,c]
        if v > value :
            c-=1
        else:
            r+=1
    return [-1,-1]

def make_matrix(n):
    # make a nxn matrix 
    return [[2*(i*n+j) for j in range(n)] for i in range(n)]

def BestTime(fn, M , value , repeats=5):
    best= float("inf")# this mean that we start at postive infintie 
    for i in range(repeats):
        t=time.perf_counter()
        fn(M,value)
        best =min(best,  time.perf_counter() - t)
    return best*1000 # make it from sec to ms 

def benchmark():
    sizes = [100, 200, 400, 800]
    print("n, linear_ms, row_binary_ms, staircase_ms")

    for n in sizes:
        m = make_matrix(n)
        missing = 2 * n * n - 1       # odd value so not in the matrix so we know worst case
        target = m[n // 2][n // 3]    # value in the matrix

        
        a = linear_search(m, target)
        b = row_BiSearch(m, target)
        c = staircase_search(m, target)
        assert a == b == c, "algorithms disagree"

        
        t1 = BestTime(linear_search, m, missing)
        t2 = BestTime(row_BiSearch, m, missing)
        t3 = BestTime(staircase_search, m, missing) 

        print(n, round(t1, 3), round(t2, 3), round(t3, 3))

def search_rotated(a, value):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == value:
            return mid
        if a[lo] <= a[mid]:              
            if a[lo] <= value < a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                            
            if a[mid] < value <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def test_rotated():
    for n in range(0, 25):
        base = list(range(0, 2 * n, 2))          
        for k in range(max(n, 1)):
            a = base[k:] + base[:k]              
            for v in range(-1, 2 * n + 1):
                expected = a.index(v) if v in a else -1
                assert search_rotated(a, v) == expected, (a, v)
    print("test pass")



test_rotated()
benchmark()



            
