
total = []
lst = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'atnon']
for j in range(len(lst)):
    for i in 'anton':
        if i not in lst[j]: break
        else:
            lst[j] = lst[j][lst[j].index(i):]
            total.append(lst[j][0])
    if 'anton' in ''.join(total):
        print(j + 1, end = ' ')
    total.clear()