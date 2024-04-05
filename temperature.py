def tmp(t):
    '''正常解法'''
    s ,a= [],[0] * len(t)
    for i, m in enumerate(t):
        while s and t[s[-1]] < m:
            p = s.pop()
            a[p] = i - p
        s.append(i)
    return a