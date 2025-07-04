import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mymoviedb.csv')
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')

# Movies released per year
def plot_release_year():
    df['Year'] = df['Release_Date'].dt.year
    year_counts = df['Year'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    plt.plot(year_counts.index, year_counts.values, marker='o', color='blue')
    plt.title('📅 Number of Movies Released Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Popularity score distribution
def plot_popularity_distribution():
    plt.figure(figsize=(8, 5))
    plt.hist(df['Popularity'], bins=30, color='green', edgecolor='black')
    plt.title('🔥 Popularity Score Distribution')
    plt.xlabel('Popularity')
    plt.ylabel('Number of Movies')
    plt.tight_layout()
    plt.show()

#Top 10 genres
def plot_top_genres():
    genre_series = df['Genre'].dropna().str.split(', ').explode()
    genre_counts = genre_series.value_counts().head(10)

    print("\n🎭 Top 10 Genres:\n", genre_counts)
    plt.figure(figsize=(8, 5))
    plt.barh(genre_counts.index[::-1], genre_counts.values[::-1], color='orange')
    plt.title('🎭 Top 10 Genres')
    plt.xlabel('Number of Movies')
    plt.tight_layout()
    plt.show()

# Show number of movie
def show_n_movies():
    try:
        n = int(input("🎯 How many movies do you want to see?"))
        if n <= 0:
            print("⚠️ Please enter a number greater than 0.")
        elif n > len(df):
            print(f"⚠️ Only {len(df)} movies available. Showing all.")
            n = len(df)

        print(f"\n🎞️ Showing info for top {n} movies:\n")
        for i in range(n):
            movie = df.iloc[i]
            print(f"🍿 --- Movie {i+1} ---")
            print(f"🎬 Title        : {movie['Title']}")
            print(f"📅 Release Date : {movie['Release_Date'].date()}")
            print(f"🎭 Genre        : {movie['Genre']}")
            print(f"🔥 Popularity   : {movie['Popularity']}")
            print(f"⭐ Vote Average : {movie['Vote_Average']}")
            print(f"🗳️ Vote Count   : {movie['Vote_Count']}")
            print()

    except ValueError:
        print("❌ Please enter a valid number.")

# Search by movie title
def search_by_title():
    keyword = input("🔍 Enter the movie title to search: ").strip().lower()
    if not keyword:
        print("⚠️ Please enter a valid title or keyword.")
        return

    results = df[df['Title'].str.lower().str.contains(keyword, na=False)]

    if results.empty:
        print("❌ No movies found with that title.")
    else:
        print(f"\n🎯 Found {len(results)} result(s):\n")
        print(results.to_string(index=False))

# Main Menu
def main_menu():
    print("🎉 Welcome to the Netflix Movie Analyzer! Let's explore the magic of movies 🎥✨")
    while True:
        print("\n🎬✨ Netflix Movie Analysis Menu ✨🎬")
        print("=============================================")
        print("1️⃣  Show Movies Released Per Year")
        print("2️⃣  Show Popularity Score Distribution")
        print("3️⃣  Show Top 10 Genres")
        print("4️⃣  Show Info of Custom Number of Movies")
        print("5️⃣  Search Movie by Title")
        print("6️⃣  Exit")

        choice = input("👉 Enter your choice (1–6): ")

        if choice == '1':
            plot_release_year()
        elif choice == '2':
            plot_popularity_distribution()
        elif choice == '3':
            plot_top_genres()
        elif choice == '4':
            show_n_movies()
        elif choice == '5':
            search_by_title()
        elif choice == '6':
            print("🍿 Thanks for using Netflix Analyzer! Stay cozy and binge wisely. ☕")
            break
        else:
            print("🚫 Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
