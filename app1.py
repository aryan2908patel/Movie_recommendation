import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7e28cf1cbefae249bb9d4a87d88ffa94&language=en-US'.format(movie_id))
    data = response.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
    return full_path



def recommend(movie):
     movie_index = movie_dict[movie_dict['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
     recommend_movie = []
     recommend_movie_posters = []

     for i in distances[1:6]:
        movie_id = movie_dict.iloc[i[0]].movie_id
        #fetch poster from API
       # print(f"i: {i}, movie_id: {movie_id}")
        recommend_movie_posters.append(fetch_poster(movie_id))
        recommend_movie.append(movie_dict.iloc[i[0]].title)
     return recommend_movie ,recommend_movie_posters



movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movie_dict = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.header('Movie Recommender System')


selected_movie_name =  st.selectbox( 'which movie you can select?',movie_dict['title'].values)


if st.button('Recommended'):
    names,posters = recommend(selected_movie_name)
      
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

