# 🎬 Movie Recommendation System (Cosine Similarity) 
<br>
## 📌 Overview This project implements a **Movie Recommendation System** that suggests movies based on user preferences using the **Cosine Similarity** method. By analyzing movie metadata (id, genres, keywords, cast, and crew), the system finds movies that are most similar to the ones a user likes. 
<br>
## ⚙️ Features - Content-based recommendation using **cosine similarity** - Preprocessing of movie metadata (genres, keywords, cast, crew) - Interactive search: input a movie title to get top recommendations - Scalable design for large datasets (e.g., TMDB dataset) - Easy-to-understand implementation with Python libraries 
<br>
## 🧮 Methodology 1. **Data Preprocessing** - Clean and merge datasets (movies + credits). - Extract relevant features (genres, keywords, cast, crew). - Convert text data into numerical vectors using **CountVectorizer**. 2. **Vector Representation** - Each movie is represented as a feature vector. 3. **Cosine Similarity Calculation** - Compute similarity scores between movies using: \[ \text{cosine similarity}(A, B) = frac{A.B}{|A|.|B|} ] 4. **Recommendation Engine** - Given a movie title, find its vector. - Rank all other movies by similarity score. - Return the top 5 recommendations. --- 
<br>
## 🛠️ Tech Stack - **Python 3.13** - **Libraries:** Pandas, NumPy, Scikit-learn - **Dataset:** TMDB (The Movie Database)
