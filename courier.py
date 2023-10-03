
print("Welcome to our courier service!")
print("Please enter the following information to calculate the cost of sending your parcel.")

#Requesting user inputs
distance = float(input("Distance (in km): "))
parcel_type = input("Parcel type (sleeve/box/crate): ")
freight_choice = input("Freight (air/land): ")
insurance_choice = input("Insurance (full/limited): ")
gift_choice = input("Gift (yes/no): ")
priority_choice = input("Priority (yes/no): ")

#Calculating freight costs
if freight_choice == "air":
    freight_cost = distance * 0.36
else:
    freight_cost = distance * 0.25

#Calculating parcel base fee
if parcel_type == "sleeve":
    base_fee = 100
elif parcel_type == "box":
    base_fee = 150
else:
    base_fee = 400

#Calculating total cost based on user choices and inputs
total_cost = base_fee + freight_cost
print("Base costs are R",total_cost)

if insurance_choice == "full":
    total_cost += 50
else:
    total_cost += 25

if gift_choice == "yes":
    total_cost += 15

if priority_choice == "yes":
    total_cost += 100
else:
    total_cost += 20

#Total cost
print("The total cost of sending your parcel is R{:.2f}.".format(total_cost))










