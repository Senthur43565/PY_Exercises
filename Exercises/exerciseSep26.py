annual_earning = float(input('Enter your annual income:\nRs.'))
if annual_earning <= 5000:
    tax = 5
elif annual_earning <= 5000 and annual_earning <= 25000:
    tax = 10
elif annual_earning <= 25000 and annual_earning <= 50000:
    tax = 15
elif annual_earning <= 50000 and annual_earning <= 75000:
    tax = 18
else:
    tax = 25

usualTax = annual_earning * tax/100

print(f'your tax rate is {tax}%')
print(f'tax payable :{usualTax:.2f}')
