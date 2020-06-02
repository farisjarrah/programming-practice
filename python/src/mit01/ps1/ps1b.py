total_cost = 1500000.0
portion_down_payment = 0.25
current_savings = 0
annual_salary = 74000
portion_saved = 0.05
rate_of_return = 0.04
semi_annual_raise = 0.05

def return_on_savings(savings, r=0.04):
    return (savings*r)/12

month_counter = 0
down_payment_months = 0
total_payment_months = 0
down_payment_switch = False

while current_savings < total_cost:
    if month_counter > 0 and month_counter % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        print(f"month counter {month_counter}, annual salary {annual_salary}, current savings {current_savings}")
        print(f"my annual salary is increasing to {annual_salary}")
    month_counter += 1
    current_savings = current_savings + return_on_savings(current_savings, rate_of_return) + ((annual_salary/12)*portion_saved)
    if down_payment_switch:
        continue
    else:
        if current_savings > (total_cost * portion_down_payment):
            down_payment_months = month_counter
            down_payment_switch = True

total_payment_months = month_counter

print(f"It will take you {down_payment_months} months to save up for the down payment and {total_payment_months} months to save up for the whole house")
