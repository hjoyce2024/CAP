import csv
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

MAXLINES = 30
FILENAME = "movies.csv"

class Movie:
    def __init__(self, name="", genre="", rating="", length="", platform=""):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.length = length
        self.platform = platform

def add_movie():
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        rep = "yes"
        while rep.lower() == "yes":
            name = input("Film Name: ")
            genre = input("Genre: ")
            rating = input("Viewing Rating: ")
            length = input("Length: ")
            platform = input("Streaming Platform: ")
            writer.writerow([name, genre, rating, length, platform])
            rep = input("Do you want to add another movie? (yes/no): ")
        if rep.lower() == "no":
            print("Okay, thank you for adding a movie!")

def find_movie():
    user_pref = Movie(
        genre=input("What genre do you want?: "),
        rating=input("Rating?: "),
        length=input("Length?: "),
        platform=input("Streaming Platform?: ")
    )

    movies_list = []
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                movies_list.append(row)

    recommendations = []
    for movie in movies_list:
        if (user_pref.genre.lower() in movie[1].lower() and
            user_pref.rating.lower() in movie[2].lower() and
            user_pref.length.lower() in movie[3].lower() and
            user_pref.platform.lower() in movie[4].lower()):
            recommendations.append(movie)

    if recommendations:
        for movie in recommendations:
            print(Back.RED + f"We recommend: {movie[0]}")
    else:
        print("No recommendations found based on your preferences.")

def main():
    print(Back.MAGENTA + "Hello, welcome to the movie genie!!")

    answer = input("Do you want to find or add a movie? Type 0 for find, 1 for add: ")
    if answer == "0":
        find_movie()
    elif answer == "1":
        print("Thank you for adding a movie to our database!")
        add_movie()
    else:
        print("Invalid choice. Please restart and choose 0 or 1.")

if __name__ == "__main__":
    # Ensure the file exists
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Genre", "Rating", "Length", "Platform"])
    main()
