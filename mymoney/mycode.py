def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def money_balance(vydavok):
    suma_total=0
    for i in vydavok:
        suma_total += i.suma
    return suma_total