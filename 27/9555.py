with open('27_B_9555.txt') as f:
    s = f.readline().split()
    n, k = int(s[0]), int(s[1])
    sp = [int(i) for i in f.readlines()]
    t = 0
    for i in range(len(sp)):
        for j in range(len(sp)):
            if len(sp[i:j]) >= k:
                if sum(sp[i:j]) % 111 == 0:
                    t += 1
    print(t)