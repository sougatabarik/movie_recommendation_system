import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies_dict = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")

selcted_movie_name = st.selectbox(
"Which movie do you want to recommend?",
movies['title'].values)

if st.button("Recommend Movie"):
    names = recommend(selcted_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
    with col2:
        st.header(names[1])
    with col3:
        st.header(names[2])
    with col4:
        st.header(names[3])
    with col5:
        st.header(names[4])