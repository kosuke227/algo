c = 0
while True:
    c += 1
    W = int(input())
    if W == 0:
        break
    n = int(input())
    d = [0] * (W + 1)
    for i in range(n):
        v, w = map(int, input().split(','))
        for j in range(W, w - 1, -1):
            d[j] = max(d[j], d[j - w] + v)
    wgt = 0
    md = max(d)
    for i in range(W + 1):
        if md == d[i]:
            wgt = i
            break
    print("Case {0}:".format(c))
    print(md)
    print(wgt)
