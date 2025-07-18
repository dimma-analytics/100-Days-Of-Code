print("Welcome to your BOLT DRIVER PROFIT CALCULATOR!")
print("Type only digits.")
trip_distance = float(input("Enter your trip distance in (km): \n"))
fuel_price = float(input("Enter the cost of a liter of fuel (₦): \n"))
fuel_consumption = float(input("How many kilometers does your car travel per litre? \n"))
fare_charged = float(input("How much did you charge for this trip? \n"))
bolt_commission = float(input("Enter bolt's commission rate (%): \n"))
Miscellaneous_expenses = float(input("Enter any unforeseen cost: \n"))

fuel_used = trip_distance/fuel_consumption
fuel_cost = fuel_used * fuel_price
bolt_commission_calc = float((bolt_commission/100) * fare_charged)
total_profit = float(fare_charged - (fuel_cost + bolt_commission_calc + Miscellaneous_expenses))

print("Your Trip summary:")
print(f"Trip Distance: {trip_distance}km")
print(f"Fuel used: {fuel_used}litres")
print(f"Fuel cost: ₦{fuel_cost}")
print(f"Fare collected: ₦{fare_charged}")
print(f"Bolt commission ({bolt_commission}%): ₦{bolt_commission_calc}")
print(F"Miscellaneous: ₦{Miscellaneous_expenses}")

if total_profit >= 0:
 print(f"Total profit: ₦{total_profit}")
 print(f"You made a profit on this trip!")
else:
 print(f"Total loss: ₦{total_profit}")
 print(f"Unfortunately, You did not make any profit on this trip!")

