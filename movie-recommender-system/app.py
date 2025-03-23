import pickle
import streamlit as st
from imdb import Cinemagoer
import concurrent.futures
import pandas as pd

# Initialize the Cinemagoer object
ia = Cinemagoer()

# Cache for poster URLs
@st.cache_data(ttl=3600)
def get_poster_url(movie_title):
    try:
        movies = ia.search_movie(movie_title)
        if movies:
            movie = ia.get_movie(movies[0].movieID)
            if movie.get('full-size cover url'):
                return movie['full-size cover url']
            elif movie.get('cover url'):
                return movie['cover url']
    except Exception as e:
        st.error(f"Error fetching poster for {movie_title}: {e}")
    return f"https://via.placeholder.com/500x750/cccccc/000000?text={movie_title}"

def fetch_posters(movie_titles):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(get_poster_url, movie_titles))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [(movies.iloc[i[0]].title, get_credits(movies.iloc[i[0]])) for i in distances[1:21]]
    recommended_movie_posters = fetch_posters([movie[0] for movie in recommended_movies])
    return recommended_movies, recommended_movie_posters

def get_credits(movie_row):
    credits = []
    for cast_member in credit_cast:
        name = cast_member.get('name', 'Unknown')
        character = cast_member.get('character', 'Unknown')
        credits.append(f"{name} as {character}")
    return " | ".join(credits[:5])

# Load data
@st.cache_resource
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

@st.cache_resource
def load_credits():
    with open('credit_cast.pkl', 'rb') as f:
        return pickle.load(f)

movies, similarity = load_data()
credit_cast = load_credits()

# Debug: Check available columns
st.write("Available columns in movies DataFrame:", movies.columns)

# Fix for KeyError: 'popularity'
def preload_popular_posters():
    if 'popularity' in movies.columns:
        popular_movies = movies.sort_values(by='popularity', ascending=False).head(100)['title'].tolist()
    elif 'vote_average' in movies.columns:  # Alternative column
        popular_movies = movies.sort_values(by='vote_average', ascending=False).head(100)['title'].tolist()
    else:
        st.error("No suitable column ('popularity' or 'vote_average') found for sorting.")
        return []
    return fetch_posters(popular_movies)

# Run preloading in the background
import threading
threading.Thread(target=preload_popular_posters, daemon=True).start()

# Streamlit UI
st.markdown('<p class="title-font">Movie Recommender System</p>', unsafe_allow_html=True)
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        recommended_movies, recommended_movie_posters = recommend(selected_movie)
    
    for row_start in range(0, 20, 5):
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.markdown(f'<p class="big-font">{recommended_movies[row_start + i][0]}</p>', unsafe_allow_html=True)
                st.image(recommended_movie_posters[row_start + i], use_column_width=True)
                st.markdown(f'<p class="credit-font">Top Cast:<br>{recommended_movies[row_start + i][1]}</p>', unsafe_allow_html=True)

st.sidebar.info('This app uses IMDb data to fetch movie posters.')
