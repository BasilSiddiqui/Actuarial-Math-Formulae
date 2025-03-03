def Present_Value (P,i,n):
    v = (1/(1+i))**n
    a = (1-v**n)/i
    return (P * a)

Present_Value(1500,0.08,6)

def Future_Value (P,i,n):
    numerator = ((1+i)**n)-1
    denominator = i
    return P*(numerator/denominator)

Future_Value(25000, 0.02, 10)

def Simple_Interest (P,i,n):
    return P*(1+(i*n))

Simple_Interest(100,0.1, 5)

def Compound_Interest (P,i,n):
    return P*(1+i)**n

Compound_Interest(100, 0.1, 5)

