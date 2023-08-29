# https://www.acmicpc.net/problem/2903

s = input()
n = int(s)
base = 2
addition = 1
for i in range(1, n + 1):
    base = base + addition
    addition *= 2
print(pow(base, 2))
