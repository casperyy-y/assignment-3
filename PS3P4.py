make = input("Enter car make ")
model = input("Enter car model ")
msrp = float(input("Enter MSRP "))
discount_percent = float(input("Enter discount percent (as a decimal) "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print("Car Make: ", make)
print("Car Model: ", model)
print("MSRP: ", msrp)
print("Discount Percent: "， discount_percent * 100，"%")
print("Amount Off: ", amount_off)
print("Discounted Price: ", discount_price)
