#input phase
books = int(input("Enter number of books:"))
cost = float(input("Enter cost per book:"))

#process phase
order_total = books * cost

if order_total>50:
 shipping = 0
else:
 shipping = 25 

#output phase
print("Order total:", order_total)
print("Shipping charge:", shipping)