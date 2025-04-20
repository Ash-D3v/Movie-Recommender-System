# 🎬 Movie Recommender System 🍿

Welcome to the Movie Recommender System! This project uses content-based filtering to suggest movies similar to the ones you love.

## 🌟 Features

- 📊 Utilizes TMDB dataset for comprehensive movie information
- 🔍 Content-based recommendation using cosine similarity
- 🖼️ Displays movie posters fetched from IMDb
- 👥 Shows top cast members for each recommended movie
- 🚀 Built with Streamlit for a smooth user interface

## 🛠️ Technologies Used

- Python 3.9+
- Streamlit
- Pandas
- Scikit-learn
- IMDbPY

## 🚀 Getting Started

### Dataset

This project uses the TMDB 5000 Movie Dataset from Kaggle. To get started:

1. Download the following files from [Kaggle TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata):
   - `tmdb_5000_credits.csv`
   - `tmdb_5000_movies.csv`

2. Place these files in your project directory.

3. Use Jupyter Notebook to open and process the data. You can start with the provided `Untitled.ipynb` notebook or create a new one.

### Data Processing

In your Jupyter Notebook, you can use the following code to load the data:

```python
import pandas as pd

# Load the movies data
movies_df = pd.read_csv('tmdb_5000_movies.csv')

# Load the credits data
credits_df = pd.read_csv('tmdb_5000_credits.csv')

# Merge the dataframes if needed
merged_df = movies_df.merge(credits_df, on='id')

# Now you can start processing and analyzing the data
```

Make sure to explore the data, handle any missing values, and perform necessary preprocessing steps before building your recommendation system.

### Installation

1. Clone the repository:
   ```
   [git clone https://github.com/Ash-D3v/Movie-Recommender-System.git}
   cd movie-recommender-system
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## 🎯 How It Works

1. Select a movie from the dropdown menu.
2. Click "Show Recommendation" to get similar movie suggestions.
3. Browse through the recommended movies, complete with posters and cast information.

## 📁 Project Structure

- `app.py`: Main Streamlit application
- `movie_list.pkl`: Preprocessed movie data
- `similarity.pkl`: Precomputed similarity matrix
- `credit_cast.pkl`: Cast information for movies

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page] https://github.com/Ashutoshdas-dev/Movie-Recommender-System.

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 🙏 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the movie dataset
- [IMDb](https://www.imdb.com/) for movie posters and additional information
- [Streamlit](https://streamlit.io/) for the awesome web app framework

---

Made with ❤️ by Ashutosh
