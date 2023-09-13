
import csv

# Define the movie data as a list of dictionaries
movies = [
    {"language": "malayalam", "name": "2018", "rating": 5, "year": 2023, "genres": ["mystery"]},
    {"language": "malayalam", "name": "aadujeevitahm", "rating": 5, "year": 2023, "genres": ["fiction", "drama"]},
    {"language": "malayalam", "name": "neymar", "rating": 4, "year": 2023, "genres": ["action", "comedy", "romance"]},
    {"language": "malayalam", "name": "sunny", "rating": 4, "year": 2022, "genres": ["drama", "thriller"]},
    {"language": "malayalam", "name": "12th man", "rating": 3, "year": 2022, "genres": ["drama", "thriller"]},
    {"language": "thamil", "name": "vikram", "rating": 5, "year": 2022, "genres": ["action", "thriller"]},
    {"language": "thamil", "name": "jai bhim", "rating": 5, "year": 2021, "genres": ["mystery", "crime"]},
    {"language": "hindi", "name": "pathaan", "rating": 5, "year": 2023, "genres": ["action", "thriller"]},
    {"language": "telungu", "name": "kgf", "rating": 5, "year": 2018, "genres": ["action", "romance", "thriller"]}
]

# Save the movie data to a CSV file
filename = "movies.csv"
fieldnames = ["language", "name", "rating", "year", "genres"]

with open(filename, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(movies)

print("Movie data has been saved to movies.csv.")

# Read and print all movies from the CSV file
print("All movies:")
with open(filename, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"])

# Print the top-rated movie with genres "mystery"
print("Top-rated movie with genres 'mystery':")
top_rated_mystery = max(movies, key=lambda x: x["rating"] if "mystery" in x["genres"] else -1)
print(top_rated_mystery)
#print only top rated movie
print("Top-rated movie :")
sort = sorted(movies, key=lambda x: x["rating"], reverse=True)
toprated_movies=max(sort,key=lambda x:x["rating"])

print(toprated_movies)

# Print the movies released in 2023
print("Movies released in 2023:")
released_2023 = [movie for movie in movies if movie["year"] == 2023]
print(released_2023)

# Sort movies by rating
sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
print("Movies sorted by rating:")
for movie in sorted_movies:
    print(movie)

# Print Malayalam movies
print("Malayalam movies:")
malayalam_movies = [movie for movie in movies if movie["language"] == "malayalam"]
print(malayalam_movies)

