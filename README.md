# Movie Recommender System

## Project Overview

The Movie Recommender System is a web application that suggests movies based on a user's input. The recommendation engine utilizes Natural Language Processing (NLP) techniques to analyze and compare movie descriptions. The project includes:

- Data cleaning and preprocessing
- Feature extraction using TF-IDF Vectorizer
- Similarity computation using Cosine Similarity
- A web application built with Flask and Jinja2 templates for user interaction

![Alt text](https://github.com/mananvijay72/movie-recommender-system/blob/main/images/recommendimage.PNG)

## Project Details

1. **Data Cleaning & Preprocessing:**
   - **Data Cleaning**: Extracted useful information from the dataset.
   - **Preprocessing**: Applied Porter Stemming, removed stop words, punctuation, and converted text to lowercase.

2. **Feature Extraction:**
   - **TF-IDF Vectorizer**: Used to convert the preprocessed text data into numerical vectors for similarity analysis.

3. **Recommendation System:**
   - **Cosine Similarity**: Computed the similarity between movie descriptions to recommend similar movies.

4. **Web Application:**
   - **Flask**: Used to create a web server.
   - **Jinja2 Templates**: Used for rendering HTML pages.
   - **HTML & CSS**: Styled and structured the user interface.

5. **Dataset:**
   - The dataset used for this project is the TMDb (The Movie Database) dataset. It contains information about 15,000+ movies and includes movie titles, release dates, genres, and overviews.
    - adult: type of move
    - : photo path of backdrop, you can access with https://image.tmdb.org/t/p/w500/{backdrop_path}
    - movie_id : id of movie on tmdb
    -  original_language: original language of movie
    - original_title: native title of movie
    - overview : movie plot description
    - popularity:
    - poster_path
    - release_date:
    - title : name of the movie
    - video:
    - vote_average:
    - vote_count:
    - genres : genres of movie
    - keywords : a short phrase attached to a title (e.g. movie / series / episode) that describes it in some way
    - cast : all the casts worked in movie
    - crew : details of all crew who involved in movie


6. **Deployment:**
   - The web application is deployed on AWS EC2 with ECR Docker image.
   - The CI/CD pipeline is set up and deployed using github action.
![Alt text](https://github.com/mananvijay72/movie-recommender-system/blob/main/images/cicd.PNG)
![Alt text](https://github.com/mananvijay72/movie-recommender-system/blob/main/images/ec2.PNG)
![Alt text](https://github.com/mananvijay72/movie-recommender-system/blob/main/images/ecr.PNG)



## Installation
 - pip install -r requirements.txt

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mananvijay72/movie-recommender-system
    cd movie-recommender-system
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Docker Image**

    ```bash
    docker pull mananvijay/movie:latest
    ```

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Use the input field to enter a movie title and click the "Get Recommendations" button.
3. View the recommended movies displayed with their posters.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for the web application.
- `static/`: Contains CSS files for styling.
- `movies.csv`: The dataset containing movie information.
- `cosine_sim.npy`: Precomputed cosine similarity matrix (saved as a NumPy array).



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The movie dataset and movie poster links were obtained from TMDb (The Movie Database).
- NLTK and scikit-learn for their valuable libraries used in text processing and machine learning.
- Flask for the web framework.

