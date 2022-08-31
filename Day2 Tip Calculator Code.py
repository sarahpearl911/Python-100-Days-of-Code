print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much would you like to tip? 15, 20, or 25? "))
people = float(input("How many people will be splitting the bill? "))

tip_percent = tip / 100 + 1
total_w_tip = total * tip_percent
amount_per_person = "{:.2f}".format(total_w_tip / people)
print(f"Each person should pay: ${amount_per_person}")
