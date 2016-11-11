
L = []
L = map(int, raw_input().split())
imax = max(L)
imin = min(L)
Sum = sum(L)
print Sum - imax, Sum - imin
