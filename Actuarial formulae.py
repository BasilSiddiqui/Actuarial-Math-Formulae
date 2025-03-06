def Simple_Interest (P,i,n):
    return P*(1+(i*n))

Simple_Interest(100,0.1, 5)

def Compound_Interest (P,i,n):
    return P*(1+i)**n

Compound_Interest(100, 0.1, 5)

def V (i): # Discount factor
    return 1/(1+i)

V(0.1)

def D (i): # Discount rate
    return i/(1+i)

D(0.1)

def PV (P,i,n): # Present value
    numerator = 1 - V(i)**n
    denominator = i
    return P*(numerator/denominator)

PV(1500,0.08,6)

def FV (P,i,n): # Future value
    numerator = ((1+i)**n)-1
    denominator = i
    return P*(numerator/denominator)

FV(25000, 0.02, 10)

def PV_growing_annuity (P,i,k,n):
    numerator = 1 - ((1+k)/(1+i))**n
    denominator = i - k
    return P*(numerator/denominator)

PV_growing_annuity(22000000, ((1.11)**(1/12))-1, 0.015, 24)
