# seeds.py
from models import Restaurant, Customer, Review, session

# Create sample data for restaurants, customers, and reviews

# Create two restaurant objects with names and prices
res1 = Restaurant(name="Shadle", price=5000)
res2 = Restaurant(name="Kibandaski", price=100)

# Create two customer objects with first names and last names
customer1 = Customer(first_name="Adrian", last_name="Munandi")
customer2 = Customer(first_name="Isaac", last_name="Kobonyo")

# Create three review objects associating customers with restaurants and providing star ratings
review1 = Review(customer=customer1, restaurant=res1, star_rating=3)
review2 = Review(customer=customer1, restaurant=res2, star_rating=5)
review3 = Review(customer=customer2, restaurant=res1, star_rating=4)

# Add all created objects to the session to prepare them for database insertion
session.add_all([res1, res2, customer1, customer2, review1, review2, review3])

# Commit the changes to the database to persist the sample data
session.commit()