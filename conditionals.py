'''
score = 41

if score >= 70:
   print("A")
elif score >= 50 and score  < 69:
   print("B")
elif score > 40 and < 45:
   print("C")
'''


"""
Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
1. Customers with a loyalty card get a 10% discount.
2. If the customer's order amount is above 20,000 NGN:
    - Loyalty card holders get an additional 5% discount.
    - Non-loyalty card holders get a free soft drink instead.
3. Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
1. Calculates the final discount or freebie for the customer.
2. Stores the result in a dictionary called `order_summary`.
3. Prints out a summary for the cashier.
"""

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

discount = 0
freebie = None

if customer["loyalty_card"]:
   discount += 10
   
   if customer["order_amount"] > 20000:
        discount +5 
else:
   if customer["order_amount"] > 20000:
      freebie = "free soft Drink" 
if customer["is_student"]:
    discount +5

final_discount_amount = (discount / 100) * customer["order_amount"]
final_amount = customer["order_amount"] - final_discount_amount

order_summary = {
      "customer_name": customer["name"],
      "initial_amount": customer["order_amount"],
      "total_discount_percent": discount,
      "final_amount_to_pay": final_amount,
      "freebie": freebie
  } 
 
print(f"Customer Name : {order_summary['customer_name']}")
print(f"Initial Amount : {order_summary['initial_amount']}")
print(f"Total Discount : {order_summary['total_discount_percent']}%")
print(f"Final Amount : {order_summary['final_amount_to_pay']:.2f}")
 
if order_summary["freebie"]:
      print(f"Freebie : {order_summary['freebie']}")
else:
   print("Freebie : None")


