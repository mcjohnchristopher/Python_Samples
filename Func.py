h = raw_input("Enter Hours:")
hours = float(h)
r = raw_input("Enter Rate")
rate = float(r)
def computepay(hours,rate):
    if hours < 41 : pay = hours * rate
    else : 
            pay = hours * rate + ((hours - 40) * (rate *.5))
    return pay

print computepay(hours,rate)