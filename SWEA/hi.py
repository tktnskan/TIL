def solve(n):
    if n%2 == 0:
        a = int(n / 2) - 1
        b = n - a
        c = []
        for i in str(a):
            c.append(int(i))
        for j in str(b):
            c.append(int(j))
        return sum(c)
    else:
        a = int(n / 2)
        b = n - a
        c = []
        for i in str(a):
            c.append(int(i))
        for j in str(b):
            c.append(int(j))
        return sum(c)


solve(1140)