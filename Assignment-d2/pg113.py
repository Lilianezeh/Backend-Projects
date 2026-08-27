# ----------- 3-8 Seeing the World -----------

places = ["Japan", "Canada", "South Africa", "Italy", "Dubai"]

# Print the original list
print(places)

# Print the list in alphabetical order without changing the original list
print(sorted(places))

# Show that the original list has not changed
print(places)

# Print the list in reverse-alphabetical order without changing the original list
print(sorted(places, reverse=True))

# Show that the original list has not changed
print(places)

# Change the order of the list
places.reverse()

# Print the list to show that the order has changed
print(places)

# Change the order of the list again
places.reverse()

# Print the list to show that it is back to its original order
print(places)

# Change the list to alphabetical order permanently
places.sort()

# Print the list
print(places)

# Change the list to reverse-alphabetical order permanently
places.sort(reverse=True)

# Print the list
print(places)



# ----------- 3-9 Dinner Guests -----------

guest_list = ["naomi", "rapheal", "vincent", "precious", "emmanuel", "stanley", "victor"]

number_of_guests = len(guest_list)

print(f"I am inviting {number_of_guests} people to dinner.")


# ----------- 3-10 Every Function -----------

countries = ["Nigeria", "Canada", "Japan", "Ghana", "Italy"]

# Print the original list
print(countries)

# Access an item using its index
print(countries[0])

# Change an item
countries[0] = "Kenya"
print(countries)

# Add an item to the beginning
countries.insert(0, "Nigeria")
print(countries)

# Add an item to the end
countries.append("Dubai")
print(countries)

# Remove an item using pop()
removed_country = countries.pop()
print(removed_country)
print(countries)

# Remove an item using del
del countries[0]
print(countries)

# Find the length of the list
print(len(countries))

# Sort the list alphabetically
countries.sort()
print(countries)

# Sort the list in reverse-alphabetical order
countries.sort(reverse=True)
print(countries)

# Reverse the order of the list
countries.reverse()
print(countries)

# Use sorted() without changing the original list
print(sorted(countries))
print(countries)