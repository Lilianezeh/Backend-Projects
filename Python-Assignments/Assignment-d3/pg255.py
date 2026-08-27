# -------------------8-6. City Names--------------------------

def city_country(city, country):
    """Returns a city and country in a formatted string."""

    return f"{city}, {country}"


city_1 = city_country("Enugu", "Nigeria")
city_2 = city_country("Lagos", "Nigeria")
city_3 = city_country("London", "England")

print(city_1)
print(city_2)
print(city_3)


# -------------------8-7. Album--------------------------
def make_album(artist, title, num_songs=None):
    """Creates a dictionary containing album information."""

    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


album_1 = make_album("Davido", "Timeless")
album_2 = make_album("Burna Boy", "African Giant")
album_3 = make_album("Wizkid", "Made in Lagos")

print(album_1)
print(album_2)
print(album_3)


# Album with number of songs
album_4 = make_album("Rema", "Rave & Roses", 16)

print(album_4)


# -------------------8-8. User Albums--------------------------
def make_album(artist, title, num_songs=None):
    """Creates a dictionary containing album information."""

    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


while True:
    print("\nEnter album information.")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist name: ")

    if artist.lower() == "q":
        break

    title = input("Album title: ")

    if title.lower() == "q":
        break

    album = make_album(artist, title)

    print(album)
    





