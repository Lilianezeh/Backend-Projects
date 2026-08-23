# -------------------8-12. Sandwiches--------------------------
def make_sandwich(*items):
    """Prints a summary of the sandwich being ordered."""

    print("\nSandwich order:")

    for item in items:
        print(f"- {item}")


make_sandwich("bread", "chicken", "cheese")

make_sandwich("bread", "beef", "lettuce", "tomato")

make_sandwich("bread", "chicken", "cheese", "lettuce", "tomato", "mayonnaise")



# -------------------8-13. User Profile--------------------------
def build_profile(first_name, last_name, **user_info):
    """Builds a dictionary containing information about a user."""

    user_info["first_name"] = first_name
    user_info["last_name"] = last_name

    return user_info


profile = build_profile(
    "Lilian",
    "Ezeh",
    role="Fullstack Developer",
    location="Nigeria",
    program="HackathonAfrica"
)

print(profile)



# -------------------8-14. Cars--------------------------
def make_car(manufacturer, model, **car_info):
    """Stores information about a car in a dictionary."""

    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)


