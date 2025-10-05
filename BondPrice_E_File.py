def getBondPrice_E(face, couponRate, yc):
    price = 0.0
    c = face * couponRate
    m = len(yc)
    for i in range(1, m + 1):
        if i == m:
            cf = c + face
        else:
            cf = c
        y = yc[i - 1]
        pvcf = cf * (1 + y) ** (-i)
        price = price + pvcf
    getBondPrice_E = price
    return getBondPrice_E
