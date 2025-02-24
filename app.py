import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ea116a5b3082bd1db21a74d0fb36d01f&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movies_list = sorted(list(enumerate(dist)),reverse = True,key = lambda x:x[1])[1:6]
    recommended_movie = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        #fetching poster from API
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster

movies_list1 = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list1)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommender System')

selected_movie = st.selectbox(
    'Yo bitch!',
    movies['title'].values
)

if st.button('Recommend'):
    names,poster = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])


