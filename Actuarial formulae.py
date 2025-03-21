'''
    Parameters:
        P (float): Initial payment amount.
        L (float): Loan amount (initial principal).
        X (float): Fixed annual repayment amount.
        i (float): Interest rate per period.
        n1 (int): Number of periods in the given interest rate (e.g., 12 for annual).
        n2 (int): Number of periods in the target interest rate (e.g., 1 for monthly).
        g (float): Growth rate of payments.
        n (int): Number of periods.
        m (int): Deferral periods.
        r (int): Repayment number for capital/interest breakdown.
        due (bool): If True, calculates annuity due; otherwise, annuity immediate.
'''


'''Interest'''


def Simple_Interest (P,i,n):
    return P*(1+(i*n))


def Compound_Interest (P,i,n):
    return P*(1+i)**n


def Convert_interest (i,n1,n2):
    return (1 + i) ** (n2 / n1) - 1


'''ANNUITIES'''


def v(i): # Discount factor
    return 1 / (1 + i)


def d(i): # Discount rate
    return i / (1 + i)


def PV_annuity(P, i, n, due=False):
    if i == 0:
        return P * n  # Handle zero interest rate case
    
    numerator = 1 - v(i)**n
    denominator = i
    factor = (1 + i) if due else 1  # Adjust for annuity-due
    return P * (numerator / denominator) * factor


def FV_annuity(P, i, n, due=False):
    if i == 0:
        return P * n  # Handle zero interest rate case
    
    numerator = (1 + i)**n - 1
    denominator = i
    factor = (1 + i) if due else 1  # Adjust for annuity-due
    return P * (numerator / denominator) * factor


def PV_growing_annuity(P, i, g, n):
    if i == g:
        return P * n  # Handle case where i = g
    
    numerator = 1 - ((1 + g) / (1 + i))**n
    denominator = i - g
    return P * (numerator / denominator)


def PV_perpetuity(P, i, due=False):
    return P / i if not due else P + (P / i)


def Perpetuity_value(P, i, t, due=False):
    if i == 0:
        return float('inf')  # If interest is 0, perpetuity is infinite
    
    factor = (1 + i) ** (t + 1) if due else (1 + i) ** t
    return (P / i) * factor


def PV_deferred_annuity(P, i, n, m, due=False):
    return (v(i)**m) * PV_annuity(P, i, n, due)


def FV_deferred_annuity(P, i, n, m, due=False):
    return ((1 + i)**m) * FV_annuity(P, i, n, due)


'''LOANS'''


def Repayment (L,i,n):
    numerator = L
    denominator = PV_annuity(1, i, n)
    return numerator / denominator


def Capital_outstanding (X,i,n,r):
    return X * PV_annuity(1, i, n-r)


def Capital_content (X,i,n,r):
    return i * X * PV_annuity(1, i, n+1-r)


def Interest_content (X,i,n,r):
    return X - Capital_content(X, i, n, r)


'''YEILDS'''


def Linear_interpolation(A,B,func):
    def f(x):
        return eval(func, {"x": x})
    fA = f(A)
    fB = f(B)
    return ((0-fB)/(fA-fB))*(A-B) + B

Linear_interpolation(0.03, 0.04, "1000000 * (1 + (1+x)**-1 + (1+x)**-2) + ((1+x)**-4) * ((1 - (1+x)**-20) / x) * 250000")