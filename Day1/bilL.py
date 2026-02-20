'''
Generate a bill 
'''
cust_id = 1
pro_Price =500
quantity = 5
coupon = True
pyMethod = input("Enter payment method: ").upper()
discount=500
total = pro_Price * quantity
#if coupon => true and total > 2000 then total = total - 500
if(coupon):
    if(total>2000):
        total-=discount

gst = total * 0.18
total=total+gst
if(pyMethod=="UPI"):
    total+=40
elif(pyMethod=="CASH"):
    total+=10
else:
    total+=50

print(f"Customer ID is {cust_id}")
print(f"Product price is {pro_Price}")
print(f"Quantity is {quantity}")
print(f"Coupon is {coupon}")
print(f"Payment method is {pyMethod}")
print(f"Discount is {discount}")
print(f"GST is {gst}")
print(f"Total amount to be paid is {total}")
