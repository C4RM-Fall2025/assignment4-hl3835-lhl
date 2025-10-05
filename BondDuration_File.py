
def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    c = face * couponRate / ppy
    r = y / ppy
    pvSum = 0.0
    wSum = 0.0
    for i in range(1, n + 1):
        if i == n:
            cf = c + face
        else:
            cf = c
        pvcf = cf * (1 + r) ** (-i)
        pvSum = pvSum + pvcf
        wSum = wSum + pvcf * i
    getBondDuration = wSum / pvSum
    return getBondDuration

