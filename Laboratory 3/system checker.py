gross_earning = 5000




if 0 <= gross_earning <= 10417:
    withholding_tax = 0.00
elif 10418 <= gross_earning <= 16666:
    withholding_tax = (0.15 * (gross_earning - 10417))
elif 16667 <= gross_earning <= 33332:
    withholding_tax = 937.50 + (0.20 * (gross_earning - 16666))
elif 33333 <= gross_earning <= 83332:
    withholding_tax = 4270.70 + (0.25 * (gross_earning - 33332))
elif 83333 <= gross_earning <= 333332:
    withholding_tax = 16770.70 + (0.30 * (gross_earning - 83332))
else:
    withholding_tax = 91770.70 + (0.35 * (gross_earning - 333332))

print(f"Withholding Tax: {withholding_tax: .2f}\n")


if (gross_earning < 10000):
    philhealth_contrib = 10000 * 0.05
elif (10001 <= gross_earning <= 99999.99):
    philhealth_contrib = gross_earning * 0.05
else:
    philhealth_contrib = 100000 * 0.05

print(f"PhilHealth Contribution: {philhealth_contrib: .2f}\n")