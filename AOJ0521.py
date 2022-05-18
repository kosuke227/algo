c = [500, 100, 50, 10, 5, 1]
while True:
    m = 1000 - int(input())
    if m == 1000:
        break
    a = 0

    for i in c:
        a += m // i
        m %= i
    print(a)

# それぞれcで割ったあまりを更新していく
