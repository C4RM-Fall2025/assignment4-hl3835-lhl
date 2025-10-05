
def getBondDuration(y, face, couponRate, m, ppy = 1):
    sum = 0.0
    cf = face * couponRate / ppy
    for i in range(1, m * ppy + 1):
        if i == m * ppy:
            pvcf = (cf + face) * (1 + y / ppy) ** (-i)
        else:
            pvcf = cf * (1 + y / ppy) ** (-i)
        sum = sum + pvcf
    getBondPrice = sum
    return getBondDuration


