#hm1289, solution from 2022
import time

def solve(n):
    """
    Creates triangular array, precomputes row sums, and then searches all
    subtriangles to determine the min sum. Each subtriangle in the nested
    for loop has vertices (i, j), (i + k, j), & (i + k, j + k).
    """
    ans, mtrx = 2**20, populate(n)
    sums = []

    for i in range(n):
        sums.append(find_subsums(mtrx[i]))

    for i in range(n):
        for j in range(i + 1):
            curr = mtrx[i][j]
            for k in range(n - i):
                if k > 0:
                    curr += sums[i + k][j + k]
                    if j != 0:
                        curr -= sums[i + k][j - 1]
                ans = min(curr, ans)

    return ans

def populate(n):
    """
    Takes as input an integer n. Returns a double array of size n x n
    containing the first n*(n+1)/2 elements of the Linear Congruential
    Generator.
    """
    prev, ans = 0, []
    for k in range(n):
        ans.append([])
        for _ in range(k + 1):
            prev = (615949 * prev + 797807) % 2**20
            entry = prev - 2**19
            ans[k].append(entry)
    return ans

def find_subsums(arr):
    """
    Takes as input an array arr. Returns an array of equivalent length
    whose entries are the partial sums of array arr.
    """
    if len(arr) == 0:
        return []
    ans, i = [arr[0]], 1
    while i < len(arr):
        ans.append(ans[i - 1] + arr[i])
        i += 1
    return ans

start = time.time()
N = 1000
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))