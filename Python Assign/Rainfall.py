inch_rainfall_amount_int = input("Enter amount of rainfall in inches: ")
inch_rainfall_amount = int(inch_rainfall_amount_int)
inch_rainfall_amounts = float(inch_rainfall_amount)
acre_sqft = 43560
gallons_per_cubic_ft = 7.48
gallons = float (inch_rainfall_amounts * acre_sqft) * gallons_per_cubic_ft
print(gallons)