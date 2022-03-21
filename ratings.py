"""Restaurant rating lister."""
'''The Tavern:3'''

# put your code here
import sys
restaurant_file = open(sys.argv[1])

restaurants_data = {}
for restaurant in restaurant_file:
    restaurant_rating = restaurant.split(":")
    # print(restaurant_rating)

    name, rating = restaurant_rating
    restaurants_data[name] = restaurants_data.get(name,rating)
# print(restaurants_data) 

# sorted_restaurants = sorted(restaurants_data.items())

for restaurant in sorted(restaurants_data):
    print(restaurant, restaurants_data[restaurant])

new_name = input("What is the restaurant name? ")

while True:
    rating = input("What is the score? ")
    if int(rating) < 1 or int(rating) > 5:
        print("This is invalid. The rate should be between 1 and 5. ")
    else:
        break

restaurants_data[new_name] = rating
    
for restaurant in sorted(restaurants_data):
    print(restaurant, restaurants_data[restaurant])


