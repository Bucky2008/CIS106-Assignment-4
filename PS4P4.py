#input phase
name = input("Enter appliance name:")
cost = float(input("Enter cost of appliance:"))

#process phase
if cost > 1000:
   warranty = cost * 0.10
else:
   warranty = cost * 0.05

total = cost + warranty 

#output phase 
print("Appliance:", name)
print("Cost:", cost)
print("Warranty:", warranty)
print("Total:", total)