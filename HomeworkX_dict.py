import sys


# def getkey(dic, value):
#     for k in dic.keys():
#         if value in dic[k]:
#             return k


n = int(input())
d = dict()
for i in range(n - 1):
    a = input().split()
    if a[1] not in d.keys():
        d[a[1]] = []
    if a[0] not in d.keys():
        d[a[0]] = []
    d[a[1]].append(a[0])
# data = list(map(str.rstrip, sys.stdin))
# print(d, data)
# type = "0"
def dfs(started):
    visited = set()
    visited.add(started)
    _dfs(visited, started)
    return len(visited) - 1


def _dfs(visited, started):
    if started in d:
        for v in d[started]:
            if v in visited:
                pass
            else:
                visited.add(v)
                _dfs(visited, v)

d = dict(sorted(d.items()))

for i in d.keys():
    print(i, dfs(i))