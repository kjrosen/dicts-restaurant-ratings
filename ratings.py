"""Restaurant rating lister."""
'''The Tavern:3'''

# put your code here
import sys
restaurant_file = open(sys.argv[1])

restaurants_data = {}
for restaurant in restaurant_file:
    restaurant_rating = restaurant.split(":")
    restaurants_data[restaurant_rating[0]] = restaurants_data[1]
print(restaurants_data)   


    


