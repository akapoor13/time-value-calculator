def calculator_present_value(cashflow, discountRate, n):
    return cashflow/((1+discountRate)**n)


def calculator_future_value(cashflow, discountRate, n):
    return cashflow*((1+discountRate)**n)
