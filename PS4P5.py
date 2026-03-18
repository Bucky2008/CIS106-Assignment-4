#input phase 
last_name = input("Enter last name:")
dependents = int(input("Enter number of dependents:"))
gross_income = float(input("Enter gross income:"))

#process phase
adjusted_income = gross_income - (dependents * 12000)

if adjusted_income > 50000:
    tax_rate = 0.20
else:
  tax_rate = 0.10

income_tax = adjusted_income * tax_rate

if income_tax < 0:
    income_tax = 100

#output phase
print("Last name:", last_name)
print("Gross income:", gross_income)
print("Dependents:", dependents)
print("Adjusted gross income:", adjusted_income)
print("Income tax:", income_tax)