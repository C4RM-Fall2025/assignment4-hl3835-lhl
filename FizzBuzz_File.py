

def FizzBuzz(start, finish):
    m = finish - start + 1
    fb = []
    for i in range(m):
        num = start + i
        if (num % 3 == 0) and (num % 5 == 0):
            fb.append("fizzbuzz")
        elif num % 3 == 0:
            fb.append("fizz")
        elif num % 5 == 0:
            fb.append("buzz")
        else:
            fb.append(num)
    FizzBuzz = fb
    return FizzBuzz

