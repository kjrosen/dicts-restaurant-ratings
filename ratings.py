"""Restaurant rating lister."""
'''The Tavern:3'''

# put your code here
import sys
restaurant_file = open(sys.argv[1])

restaurants_data = {}
for restaurant in restaurant_file:
    restaurant_rating = restaurant.split(":")
    print(restaurant_rating)

    name, rating = restaurant_rating
    restaurants_data[name] = restaurants_data.get(name,rating)
print(restaurants_data) 

for restaurant in restaurants_data:
    sorted(restaurants_data.items())


    


