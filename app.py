import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np


def recommend(movie):
     movie_index = movie_dict[movie_dict['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])[1:6]
     recommend_movie = []

     for i in distances:
        movie_id = i[0]
        recommend_movie.append(movie_dict.iloc[i[0]].title)
     return recommend_movie


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movie_dict = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.header('Movie Recommender System')

selected_movie_name =  st.selectbox( 'which movie you can select?',movie_dict['title'].values)

if st.button('Recommended'):
    recommendation = recommend(selected_movie_name)
    
    for i in recommendation:
        st.write(i)