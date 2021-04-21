# no.1
def hotel_cost(nights):
    return nights*140

# no.2
def plane_ride_cost(city):
    if "Capetown" == city:
     return "2500"
    elif "Durban" == city:
        return "2300"
    elif "JHB" == city:
        return "2000"
    elif "BFN" == city:
        return "1800"


# no.3
def rental_car_cost(days):
    car_cost = 40 * days
    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 < 7:
        car_cost = car_cost - 20
    return car_cost


# no.4
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + int(plane_ride_cost(city)) + spending_money

print(trip_cost("BFN", 2, 1000))