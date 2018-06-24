cars = 100
# I have 100 cars
space_in_a_car = 4
#I can fit 4 people in 1 cars
drivers = 30
# there are 30 drivers
passengers = 90
# there are 90 passengers
cars_not_driven = cars - drivers
# this equations calulates the total amount
# of cars that are not driven
cars_driven = drivers
#this is the total amount of cars that
# are actually utilized

carpool_capacity = cars_driven * space_in_a_car
# this is the available space for passengers
# within the carpool
average_passengers_per_car = passengers/cars_driven
# this is the average available of passengers per car

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven,"empty cars today")
print ("We can transport", carpool_capacity, "people today")
print ("We have", passengers, "to carpool today")
print ("We need toput about", average_passengers_per_car, "in each car.")
