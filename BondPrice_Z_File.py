def getBondPrice_Z(face, couponRate, times, yc):
    price = 0.0
    c = face * couponRate
    m = len(times)
    for i in range(m):
        if i == m - 1:
            cf = c + face
        else:
            cf = c
        t = times[i]
        y = yc[i]
        pvcf = cf * (1 + y) ** (-t)
        price = price + pvcf
    getBondPrice_Z = price
    return getBondPrice_Z
