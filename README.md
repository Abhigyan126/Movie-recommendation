# Movie Recommendation System

## Description

The Movie Recommendation System is a user-friendly application designed to manage a collection of movies and provide personalized movie recommendations. The system allows users to add, edit, delete, search, and sort movies, as well as save and load their movie list to and from a local file. Recommendations are generated based on a custom scoring algorithm and genre probabilities derived from watched movies.

## Features

### 1. Add, Edit, and Delete Movies
- **Add Movie:** Users can add new movies to their collection by providing details such as title, genre, movie length, ML, FL, age restriction, country, and production house.
- **Edit Movie:** Users can edit the details of any selected movie in the collection.
- **Delete Movie:** Users can delete a selected movie from the collection.

### 2. Search and Sort Movies
- **Search Movie:** Users can search for a movie by title. The system highlights the searched movie in the list for easy identification, editing, or deletion.
- **Sort Movies:** Users can sort the movie list by score in ascending or descending order.

### 3. Recommend Movies
- **Recommend by Score:** The system recommends movies based on a custom scoring algorithm that evaluates various attributes of each movie.
- **Recommend by Probability:** The system recommends movies based on genre probabilities derived from the user's watched movies.

### 4. Save and Load Movies
- **Save Movies:** Users can save their movie list to a local JSON file for future use.
- **Load Movies:** Users can load a previously saved movie list from a local JSON file.

## Usage

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python installations)
- JSON library (included with Python installations)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. Run the application:
    ```bash
    python main.py
    ```

### How to Use
1. **Adding a Movie:**
   - Click the "Add Movie" button.
   - Enter the movie details in the prompted dialog and click "OK".

2. **Editing a Movie:**
   - Select a movie from the list.
   - Click the "Edit Movie" button.
   - Modify the movie details in the prompted dialog and click "OK".

3. **Deleting a Movie:**
   - Select a movie from the list.
   - Click the "Delete Movie" button.

4. **Searching for a Movie:**
   - Click the "Search Movie" button.
   - Enter the movie title in the prompted dialog and click "OK".

5. **Sorting Movies:**
   - Click the "Sort Ascending" button to sort movies by score in ascending order.
   - Click the "Sort Descending" button to sort movies by score in descending order.

6. **Recommending Movies:**
   - Click the "Recommend by Score" button to get recommendations based on custom score.
   - Click the "Recommend by Probability" button to get recommendations based on genre probabilities.

7. **Saving and Loading Movies:**
   - Click the "Save Movies" button to save the current movie list to a JSON file.
   - Click the "Load Movies" button to load a movie list from a JSON file.

### Example Movies
The system comes with a default set of movies to help you get started. These can be modified or expanded as needed.

