def mortgage_calculation(principal, interest_rate, num_years):
    p = float(principal)
    r = (float(interest_rate) / 100) / 12
    n = float(num_years) * 12
    rate = p * r * (((1 + r)**n)/(((1+r)**n)-1))
    return round(rate, 2)

print("Let's calculate your fixed monthly mortgage payments!")
print("What is the loan amount?")
principal = input()
print("What is the annual interest rate?")
interest_rate = input()
print("In years, what is the life of this loan?")
num_years = input()
mort_rate = mortgage_calculation(principal, interest_rate, num_years)
final_string = "Your mortgage payment will be ${} per month".format(mort_rate)
print(final_string)