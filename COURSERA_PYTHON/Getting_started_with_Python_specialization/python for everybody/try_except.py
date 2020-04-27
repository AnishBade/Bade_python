def computepay(h, r):
    if h <= 40:
        pay = 40 * r
    else:
        pay = 40 * r + (h - 40) * 1.5 * r
    return pay


hrs = input("Enter Hours:")

rate = input("Enter Rate")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter NUMBERS")

p = computepay(h, r)
print("Pay", p)