# mortgage.py
#
# Exercise 1.7

mortgage = float(500000)
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while mortgage > 0:
    paid = 2684.11
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        paid += extra_payment

    if mortgage < paid:
        total_paid += mortgage
        mortgage = 0
    else:
        mortgage = mortgage * (1.0 + (0.05 / 12)) - paid
        total_paid += paid

    months += 1
    print("{} {} {}".format(months, total_paid, mortgage))

print("Total paid {}".format(total_paid))
print("Months {}".format(months))

