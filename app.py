from movie_recommendation_system.constants import *
from movie_recommendation_system.utils.common import read_yaml
import streamlit as st
import pickle
import pandas as pd
import requests 

class Prediction:
    def __init__(self,config_filepath = CONFIG_FILEPATH):
        self.config = read_yaml(config_filepath)
        self.movies_dict = pd.DataFrame(pickle.load(open(self.config.prediction.movie_dict,"rb")))
        self.similarity = pickle.load(open(self.config.prediction.similarity_path,"rb"))

    def recommend(self,movie_name):
        movie_index = self.movies_dict[self.movies_dict['title'] == movie_name].index[0]
        distance = self.similarity[movie_index]
        movies_recommendation_index = sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]

        movie_recommendation_name = []
        movie_recommendation_posters = []  

        for i in movies_recommendation_index:
            movie_id = self.movies_dict.iloc[i[0]].movie_id
            movie_recommendation_name.append(self.movies_dict.iloc[i[0]].title)
            movie_recommendation_posters.append(self.fetch_poster(movie_id))

        return movie_recommendation_name,movie_recommendation_posters

    def fetch_poster(self,movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        data = response.json()
        full_poster_path =  f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        return  full_poster_path

if __name__ == "__main__":
    obj = Prediction()
    st.title("Movie Recommendation System")
    selected_option = st.selectbox("Choose or Write Movie Name.....", obj.movies_dict['title'].values)

    if st.button("Recommed"):
        movie_names,posters = obj.recommend(selected_option)

        col1, col2, col3, col4, col5 = st.columns(5,gap = 'large')

        with col1:
            st.header(movie_names[0])
            st.image(posters[0])

        with col2:
            st.header(movie_names[1])
            st.image(posters[1])

        with col3:
            st.header(movie_names[2])
            st.image(posters[2])

        with col4:
            st.header(movie_names[3])
            st.image(posters[3])

        with col5:
            st.header(movie_names[4])
            st.image(posters[4])

