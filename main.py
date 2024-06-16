import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, END, filedialog
import random
import math
import json

# Define the score function
def score(genera, movie_length, ML, FL, age_restriction, country, production_house):
    genera_arr = ['Action', 'Drama', 'Comedy', 'Horror', 'Sci-Fi']
    movie_length_arr = ['Short', 'Feature']
    ML_arr = ['60', '90', '120']
    FL_arr = ['Feature', 'Short']
    age_restriction_arr = ['G', 'PG', 'PG-13', 'R']
    country_arr = ['USA', 'UK', 'Canada', 'Australia']
    production_house_arr = ['Production X', 'Production Y', 'Production Z']
    
    custom_genera = 1.0
    custom_movie_length = 1.0
    custom_ML = 1.0
    custom_FL = 1.0
    custom_age_restriction = 1.0
    custom_country = 1.0
    custom_production_house = 1.0

    total_score = 0.0

    if genera in genera_arr:
        index = genera_arr.index(genera)
        score_genera = math.log(((index + 1) ** 2) * custom_genera)
        total_score += score_genera

    if movie_length in movie_length_arr:
        index = movie_length_arr.index(movie_length)
        score_movie_length = math.log(((index + 1) ** 2) * custom_movie_length)
        total_score += score_movie_length

    if ML in ML_arr:
        index = ML_arr.index(ML)
        score_ML = math.log(((index + 1) ** 2) * custom_ML)
        total_score += score_ML

    if FL in FL_arr:
        index = FL_arr.index(FL)
        score_FL = math.log(((index + 1) ** 2) * custom_FL)
        total_score += score_FL

    if age_restriction in age_restriction_arr:
        index = age_restriction_arr.index(age_restriction)
        score_age_restriction = math.log(((index + 1) ** 2) * custom_age_restriction)
        total_score += score_age_restriction

    if country in country_arr:
        index = country_arr.index(country)
        score_country = math.log(((index + 1) ** 2) * custom_country)
        total_score += score_country

    if production_house in production_house_arr:
        index = production_house_arr.index(production_house)
        score_production_house = math.log(((index + 1) ** 2) * custom_production_house)
        total_score += score_production_house

    return total_score

# Initialize movie list with some test movies
movies = [
    {'title': 'Movie 1', 'genera': 'Action', 'movie_length': 'Feature', 'ML': '120', 'FL': 'Feature', 'age_restriction': 'PG-13', 'country': 'USA', 'production_house': 'Production X', 'score': score('Action', 'Feature', '120', 'Feature', 'PG-13', 'USA', 'Production X')},
    {'title': 'Movie 2', 'genera': 'Drama', 'movie_length': 'Short', 'ML': '90', 'FL': 'Short', 'age_restriction': 'R', 'country': 'UK', 'production_house': 'Production Y', 'score': score('Drama', 'Short', '90', 'Short', 'R', 'UK', 'Production Y')},
    {'title': 'Movie 3', 'genera': 'Sci-Fi', 'movie_length': 'Feature', 'ML': '120', 'FL': 'Feature', 'age_restriction': 'PG-13', 'country': 'USA', 'production_house': 'Production Z', 'score': score('Sci-Fi', 'Feature', '120', 'Feature', 'PG-13', 'USA', 'Production Z')},
    {'title': 'Movie 4', 'genera': 'Comedy', 'movie_length': 'Feature', 'ML': '90', 'FL': 'Feature', 'age_restriction': 'G', 'country': 'Canada', 'production_house': 'Production X', 'score': score('Comedy', 'Feature', '90', 'Feature', 'G', 'Canada', 'Production X')},
    {'title': 'Movie 5', 'genera': 'Horror', 'movie_length': 'Short', 'ML': '60', 'FL': 'Short', 'age_restriction': 'R', 'country': 'Australia', 'production_house': 'Production Y', 'score': score('Horror', 'Short', '60', 'Short', 'R', 'Australia', 'Production Y')},
    # Add more test movies as needed
]

watched_movies = [
    {'title': 'Movie A', 'genera': 'Action'},
    {'title': 'Movie B', 'genera': 'Action'},
    {'title': 'Movie C', 'genera': 'Drama'},
    {'title': 'Movie D', 'genera': 'Sci-Fi'},
    {'title': 'Movie E', 'genera': 'Sci-Fi'},
    {'title': 'Movie F', 'genera': 'Sci-Fi'}
]

def add_movie():
    title = simpledialog.askstring("Input", "Movie Title:")
    if not title:
        return

    genera = simpledialog.askstring("Input", "Genera:", initialvalue="Action")
    movie_length = simpledialog.askstring("Input", "Movie Length:", initialvalue="Feature")
    ML = simpledialog.askstring("Input", "ML:", initialvalue="120")
    FL = simpledialog.askstring("Input", "FL:", initialvalue="Feature")
    age_restriction = simpledialog.askstring("Input", "Age Restriction:", initialvalue="PG-13")
    country = simpledialog.askstring("Input", "Country:", initialvalue="USA")
    production_house = simpledialog.askstring("Input", "Production House:", initialvalue="Production X")

    movie = {
        'title': title,
        'genera': genera,
        'movie_length': movie_length,
        'ML': ML,
        'FL': FL,
        'age_restriction': age_restriction,
        'country': country,
        'production_house': production_house,
        'score': score(genera, movie_length, ML, FL, age_restriction, country, production_house)
    }

    movies.append(movie)
    update_movie_list()

def update_movie_list():
    movie_listbox.delete(0, END)
    for movie in movies:
        movie_listbox.insert(END, f"{movie['title']} ({movie['score']:.2f})")

def edit_movie():
    selected_movie_index = movie_listbox.curselection()
    if not selected_movie_index:
        return

    selected_movie = movies[selected_movie_index[0]]
    title = simpledialog.askstring("Input", "Movie Title:", initialvalue=selected_movie['title'])
    if not title:
        return

    genera = simpledialog.askstring("Input", "Genera:", initialvalue=selected_movie['genera'])
    movie_length = simpledialog.askstring("Input", "Movie Length:", initialvalue=selected_movie['movie_length'])
    ML = simpledialog.askstring("Input", "ML:", initialvalue=selected_movie['ML'])
    FL = simpledialog.askstring("Input", "FL:", initialvalue=selected_movie['FL'])
    age_restriction = simpledialog.askstring("Input", "Age Restriction:", initialvalue=selected_movie['age_restriction'])
    country = simpledialog.askstring("Input", "Country:", initialvalue=selected_movie['country'])
    production_house = simpledialog.askstring("Input", "Production House:", initialvalue=selected_movie['production_house'])

    movies[selected_movie_index[0]] = {
        'title': title,
        'genera': genera,
        'movie_length': movie_length,
        'ML': ML,
        'FL': FL,
        'age_restriction': age_restriction,
        'country': country,
        'production_house': production_house,
        'score': score(genera, movie_length, ML, FL, age_restriction, country, production_house)
    }

    update_movie_list()

def delete_movie():
    selected_movie_index = movie_listbox.curselection()
    if not selected_movie_index:
        return

    del movies[selected_movie_index[0]]
    update_movie_list()

def recommend_movies_by_score():
    sorted_movies = sorted(movies, key=lambda x: x['score'], reverse=True)
    recommendations = sorted_movies[:5]
    display_recommendations(recommendations)

def calculate_genre_probabilities(watched_movies):
    genre_counts = {}
    for movie in watched_movies:
        genre = movie['genera']
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    total_movies = len(watched_movies)
    genre_probabilities = {genre: count / total_movies for genre, count  in genre_counts.items()}
    return genre_probabilities
def recommend_movies_by_probability():
    genre_probabilities = calculate_genre_probabilities(watched_movies)
    weighted_movies = []

    for movie in movies:
        genre = movie['genera']
        if genre in genre_probabilities:
            weighted_movies.extend([movie] * int(genre_probabilities[genre] * 100))

    recommendations = random.sample(weighted_movies, 5)
    display_recommendations(recommendations)

def display_recommendations(recommendations):
    recommendations_str = "\n".join([f"{movie['title']} ({movie['genera']})" for movie in recommendations])
    messagebox.showinfo("Recommended Movies", recommendations_str)

def save_movies():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not file_path:
        return

    with open(file_path, 'w') as file:
        json.dump(movies, file)
    messagebox.showinfo("Success", "Movies saved successfully.")

def load_movies():
    global movies
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not file_path:
        return

    with open(file_path, 'r') as file:
        movies = json.load(file)
    update_movie_list()
    messagebox.showinfo("Success", "Movies loaded successfully.")

def search_movie():
    search_title = simpledialog.askstring("Search", "Enter movie title to search:")
    if not search_title:
        return

    for i, movie in enumerate(movies):
        if movie['title'].lower() == search_title.lower():
            movie_listbox.selection_clear(0, END)
            movie_listbox.selection_set(i)
            movie_listbox.activate(i)
            messagebox.showinfo("Found", f"Movie '{movie['title']}' found and highlighted in the list.")
            return

    messagebox.showinfo("Not Found", f"Movie '{search_title}' not found.")

def sort_movies(ascending=True):
    movies.sort(key=lambda x: x['score'], reverse=not ascending)
    update_movie_list()

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

frame = tk.Frame(root)
frame.pack(pady=20)

# Listbox to display movies
movie_listbox = Listbox(frame, width=50, height=15)
movie_listbox.pack(side="left", fill="y")

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=movie_listbox.yview)
scrollbar.pack(side="right", fill="y")
movie_listbox.config(yscrollcommand=scrollbar.set)

# Buttons for various actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Movie", command=add_movie).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Edit Movie", command=edit_movie).grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Delete Movie", command=delete_movie).grid(row=0, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Recommend by Score", command=recommend_movies_by_score).grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Recommend by Probability", command=recommend_movies_by_probability).grid(row=1, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Search Movie", command=search_movie).grid(row=1, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Sort Ascending", command=lambda: sort_movies(ascending=True)).grid(row=2, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Sort Descending", command=lambda: sort_movies(ascending=False)).grid(row=2, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Save Movies", command=save_movies).grid(row=2, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Load Movies", command=load_movies).grid(row=2, column=3, padx=10, pady=5)

# Initialize the movie listbox with default movies
update_movie_list()

# Run the main event loop
root.mainloop()

