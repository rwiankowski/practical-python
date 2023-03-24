# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
extra_payment = 1000.0
extra_payment_start = 61
extra_payment_end = 108
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    total_payment = base_payment
    if months in range(extra_payment_start, extra_payment_end + 1):
        total_payment += extra_payment
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment
    if principal < 0:
        total_paid += principal
        principal = 0
    print(f'{months} {total_paid:0.2f} {principal:0.2f}')

print('Total paid', total_paid, 'over', months, 'months')