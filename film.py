import imdb

ia = imdb.Cinemagoer()

Movie = input("Enter a movie name: ")
items = ia.search_movie(Movie)
print("\nSearch results:")
for index, movie in enumerate(items):
    print(f"{index + 1}: {movie['title']} ({movie['year']})")

movie_index = int(input("\nEnter the number of the movie you want to get info for: ")) - 1
movie_id = items[movie_index].movieID
movie_info = ia.get_movie(movie_id)

print("\nMovie Information:")
print(f"Title: {movie_info.get('title')}")
print(f"Year: {movie_info.get('year')}")
print(f"Rating: {movie_info.get('rating')}")
print(f"Genres: {', '.join(movie_info.get('genres', []))}")
print(f"Directors: {', '.join(str(d) for d in movie_info.get('directors', []))}")
print(f"Cast: {', '.join(str(c) for c in movie_info.get('cast', [])[:5])}...")
print(f"Plot: {movie_info.get('plot outline')}")
print(f"Runtime: {movie_info.get('runtimes', ['N/A'])[0]} minutes")
print(f"Countries: {', '.join(movie_info.get('countries', []))}")
print(f"Languages: {', '.join(movie_info.get('languages', []))}")
