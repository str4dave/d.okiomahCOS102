def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, T):
    A = P * (1 + R / n) ** (n * T)
    return A

def annuity_plan(PMT, R, n, T):
    A = PMT * (((1 + R / n) ** (n * T) - 1) / (R / n))
    return A

    flowchat 
    # Start
    # Input: Principal amount (P), Rate of interest (R), Time period (T)
    # Calculate simple Interest: A = P * (1 + (R / 100) * T)
    # Output: simple Interest (A)
    # End

    flowchat  
    # Start
    # Input: Principal amount (P), Rate of interest (R), Number of times interest applied per time period (n), Time period (T)
    # Calculate Compound Interest: A = P * (1 + R / n) ** (n * T)
    # Output: Compound Interest (A)
    # End

    flowchat 
    # Start
    # Input: Payment amount per period (PMT), Rate of interest (R), Number of times interest applied per time period (n), Time period (T)
    # Calculate Annuity Plan: A = PMT * (((1 + R / n) ** (n * T) - 1) / (R / n))
    # Output: Annuity Plan (A)
    # End