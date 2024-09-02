from flask import Flask, request, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the movies dataset
movies = pd.read_csv('movies.csv')

# Load the cosine similarity matrix as a memory-mapped file
cosine_sim = np.load('cosine_sim.npy', mmap_mode='r')

# Function to recommend movies based on user's input
def recommend_movies(movie_name):
    # Get the index of the movie that matches the title
    movie_index = movies[movies['title'].apply(lambda x: x.lower()) == movie_name.lower()].index[0]

    # Get the similarity scores of all movies with the movie_index
    similarity_scores = list(enumerate(cosine_sim[movie_index]))
    
    # Sort the movies based on the similarity scores in descending order
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 recommended movies
    recommended_movies = [movies.iloc[i[0]] for i in sorted_movies[1:11]]

    return recommended_movies

@app.route('/')
def home():
    return render_template('home.html', movies=movies.to_dict(orient='records'))



@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form.get('movie_name')
    recommended_movies = recommend_movies(movie_name)
    return render_template('recommend.html', movie_name=movie_name, movies=recommended_movies)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)
