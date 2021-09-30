#calculator.py

def sum(m, n):

    result = m
    for i in range(abs(n)):
        if n > 0 :  result += 1
        else: result -= 1
    return result

def divide(m, n):
    if abs(n) > abs(m): return 0
    if m < 0:
        if n > 0:
            result = 0
            while (m + n <= 0):
                m += n
                result += -1
            return result
        else:
            result = 0
            while (m - n <= 0):
                m += -n
                result += 1
            return result
    else:
        if n < 0:
            result = 0
            while (m + n >= 0):
                m -= -n
                result += -1
            return result

        else:
            result = 0
            while(m - n >= 0):
                m -= n
                result += 1
            return result


# print(divide(5, -1))
#
# print(divide(-5, -1))
# print(divide(-5, 1))
# print(divide(15, 5))
# print(divide(15, -4))