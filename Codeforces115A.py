n = int(input())
d = dict()
max_level = 0
for position in range(n):
    d[position + 1] = int(input())
# for dict_index in d.keys():
#     cur_level = 1
#     if d[dict_index] > 0:
#         while True:
#             if d[dict_index] in d.keys():
#                 dict_index = d[12dict_index]
#                 cur_level += 1
#             else:
#                 break

levels = dict()


def calc_levels(d, v):
    if v not in levels:
        levels[v] = 1
        if d[v] != -1:
            levels[v] += calc_levels(d, d[v])
    return levels[v]


# max_level = max(max_level, cur_level)
print(max([calc_levels(d, i) for i in range(1, n + 1)]))
