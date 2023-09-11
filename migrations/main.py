from migrations.models import Restaurant, Customer, Review, session
from sqlalchemy.orm.exc import NoResultFound

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Create sample data for restaurants, customers, and reviews

    # Create Restaurant objects with name and price attributes
    shadle = Restaurant(name="Shadle", price=3050)
    kibandaski = Restaurant(name="Kibandaski", price=120)

    # Create Customer objects with first_name and last_name attributes
    customer1 = Customer(first_name="Adrian", last_name="Munandi")
    customer2 = Customer(first_name="Isaac", last_name="Kobonyo")
    customer3 = Customer(first_name="Sharon", last_name="Mwongeli")

    # Add the sample data to the database session and commit the changes
    session.add_all([shadle, kibandaski, customer1, customer2, customer3])
    session.commit()

    # Query the database for the fanciest restaurant
    fanciest_restaurant = Restaurant.fanciest()

    # Print the name of the fanciest restaurant
    print(f"Fanciest restaurant: {fanciest_restaurant.name}")

    shadle = session.query(Restaurant).filter_by(name="Shadle").first()

    if shadle:
        # Check if Lavender Lutta has already reviewed Shadle
        lavender_lutta_reviewed = session.query(Review).filter(
            Review.customer_id == customer3.id,
            Review.restaurant_id == shadle.id
        ).first()

        if not lavender_lutta_reviewed:
            # Lavender Lutta hasn't reviewed Shadle, so add the review
            review1 = Review(customer=customer3, restaurant=shadle, star_rating=5)
            session.add(review1)
            session.commit()
            print("Added review for Shadle by Lavender Lutta")
        else:
            # Lavender Lutta has already reviewed Shadle
            print("Lavender Lutta has already reviewed Shadle.")
    else:
        print("Shadle does not exist.")

    customer2 = session.query(Customer).filter_by(first_name="Isaac").first()

    if customer2:
        # Find Isaac Kobonyo's favorite restaurant using the favorite_restaurant method
        favorite_restaurant = customer2.favorite_restaurant()

        if favorite_restaurant:
            # Print the name of Isaac Kobonyo's favorite restaurant
            print(f"Favorite restaurant for Isaac Kobonyo: {favorite_restaurant.name}")
        else:
            # Print a message if Isaac Kobonyo has not reviewed any restaurants yet
            print("Isaac Kobonyo has not reviewed any restaurants yet.")
    else:
        # Print a message if Isaac Kobonyo does not exist
        print("Customer Isaac Kobonyo not found.")

    shadle = session.query(Restaurant).filter_by(name="Shadle").first()

    # Check if Shadle exists
    if shadle:
        # Use the count method to get the number of reviews for Shadle
        review_count = session.query(Review).filter_by(restaurant_id=shadle.id).count()

        # Print the number of reviews for Shadle
        print(f"Number of reviews for Shadle: {review_count}")
    else:
        # Print a message if Shadle does not exist
        print("Shadle does not exist.")