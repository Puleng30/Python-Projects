
def hotel_cost(num_nights):   #Function that calculates how much it costs to stay at a hotel
    price_per_night = 150     #night rate
    total_cost = num_nights * price_per_night 
    return total_cost 

def plane_cost(city_flight):  #function that calculates the cost of flying to a specific city
    if city_flight == "Johannesburg":
        return 550
    if city_flight == "Durban":
        return 490
    if city_flight == "Cape Town":
        return 650
    if city_flight == "Port Elizabeth":
        return 400
    else:
        return "Wrong city"
    
def car_rental(rental_days):  #function that calculates daily cost of renting a car
    daily_rental_cost = 230   #daily rental rate 
    total_cost = rental_days * daily_rental_cost
    return total_cost

def holiday_cost(city_flight, num_nights, rental_days):   #function that calculates total holiday costs
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

#Requesting user inputs
city_flight = input("Please enter the city you want to fly to. Options are: Johannesburg, Durban, Cape Town and Port Elizabeth: ")
num_nights = int(input("Enter the number of nights you wish to stay at the hotel for: "))
rental_days = int(input("Enter the number of days you wish to rent the car for: "))

#calculating the holiday costs
total_cost = holiday_cost(city_flight, num_nights, rental_days)

#printing all holiday information 
print("Your holiday details are:")
print("Destination: ", city_flight)
print("Flight cost: R", plane_cost(city_flight))
print("Hotel cost: R", hotel_cost(num_nights))
print("Car rental cost: R", car_rental(rental_days))
print("Total cost: R", total_cost)