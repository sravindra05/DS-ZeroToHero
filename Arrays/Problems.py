'''
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.
'''


def maxArea(heights):
    if(len(heights) > 0):
        p = 0
        m = len(heights)-1
        area = 0
        while(p < m):
            c = min(heights[p], heights[m])*(m-p)
            if c > area:
                area = c
            if(heights[p] > heights[m]):
                m -= 1
            else:
                p += 1
        return area


'''
Rearrange array numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
'''


def nextPermutation(a):
    """
    Does not return anything, modifies nums in-place instead.
    """
    i = len(a)-1
    while(i > 0 and a[i] <= a[i-1]):
        i -= 1
    print(i)
    i -= 1
    if i < 0:
        a.reverse()
        return None
    j = len(a)-1
    while(j > 0 and a[j] <= a[i]):
        j -= 1
    t = a[j]
    a[j] = a[i]
    a[i] = t
    k = a[i+1:]
    k.reverse()
    a[i+1:] = k
