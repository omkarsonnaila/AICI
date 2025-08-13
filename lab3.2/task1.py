def calculate_compound_interest():
    """
    Calculates compound interest based on principal, rate, time, and number of times interest is compounded per year.

    Example:
        Input:
            Principal: 1000
            Rate: 5
            Time: 2
            Compounded per year: 4
        Output:
            Compound Interest: 104.486
    """
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    n = int(input("Enter the number of times interest is compounded per year: "))

    amount = principal * (1 + rate/(100*n))**(n*time)
    compound_interest = amount - principal
    print(f"Compound Interest: {compound_interest:.3f}")

calculate_compound_interest()