ln = "0123456789ABCDEF"


def to_base(base, x):
    if base == 10:
        print(x)
        return

    res = []
    aft_res = []

    if '.' in str(x):
        after = float(f"0{str(x)[str(x).index('.'):]}")
        x = int(str(x)[:str(x).index('.')])
        for i in range(3):
            aft_res.append(ln[int(after * base)])
            after *= base
            after = float(f"0{str(after)[str(after).index('.'):]}")

    while x // base:
        res.append(ln[x % base])
        x //= base
    res.append(x)
    res.reverse()
    print(f"Answer: {''.join([str(i) for i in res])}.{''.join([str(i) for i in aft_res])}")


def to_decimal(num, frommns, tons):
    if '.' in str(num):
        ind = -1
        before = int(str(num)[:num.index('.')], int(frommns))
        after = 0
        for i in str(num)[num.index('.')+1:]:
            after += ln.index(i) * int(frommns)**ind
            ind -= 1
        numa = float(before) + after
    else:
        numa = int(str(num), int(frommns))
    to_base(int(tons), numa)


while True:
    print("Введите число, исходную систему, целевую систему:")
    data = input().split()
    to_decimal(data[0], data[1], data[2])
