def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    c = face * couponRate / ppy
    r = y / ppy 
    price = 0
    for i in range(1, n + 1):
        if i == n:
            cf = c + face 
        else:
            cf = c
        price = price + cf * (1 + r) ** (-i)
    return price
    
