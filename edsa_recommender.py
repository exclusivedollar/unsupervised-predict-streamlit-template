"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
import numpy as np
# Data handling dependencies
import pandas as pd
# Streamlit dependencies
import streamlit as st

from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import recommenders.collaborative_based as collab
from utils.data_loader import load_movie_titles
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","Interactive Movie Recommender","About Team 2","Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[1:300])
        movie_2 = st.selectbox('Second Option',title_list[550:555])
        movie_3 = st.selectbox('Third Option',title_list[311:540])

        # movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        # movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        # movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------
    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Add eda")


    if page_selection == "Interactive Movie Recommender":

        # Setting up background image:
        st.image('resources/imgs/background.jpg', width=800)

        st.info('Still need to make this all look nice and maybe add some more functionality')

        st.title("Interactive Movie Recommender")
        st.markdown('## Insert subheader')
        st.write("Filter movies below then search your top pics on youtube through the search bar below")

        with st.beta_container():
            # Load movies.csv dataframe:
            movies_df = pd.read_csv('resources/data/movies.csv', index_col='movieId')

            # Year selection
            st.subheader('Enter your preferred year-range')
            start_year = st.slider("Start Year", 1874, 2019)
            end_year = st.slider('End Year', start_year, 2019)
            movies_df = movies_df[(movies_df['year']>=start_year) & (movies_df['year']<=end_year)]

            # Genre selection
            st.subheader('Enter your preferred genres')
            genres_list = ['Documentary', 'Animation','Film-Noir','Romance','Adventure',
            'Western','Children','Sci-Fi','Drama','Thriller',
            'Mystery','War','Comedy','Action','IMAX','Musical','Fantasy','Horror','Crime']
            genres = list(st.multiselect('Select genres', genres_list))
            
            drop_rows = []
            for index, row in movies_df.iterrows():
                if set(genres).issubset(set(row['genres'].split())):
                    pass
                else:
                    drop_rows.append(index)
            
            movies_df = movies_df.drop(drop_rows)




            st.dataframe(movies_df)

        with st.beta_container():
            st.subheader('Search YouTube')
            st.text('Descriptive text')
            st.components.v1.html(
                """
                <form action="http://www.youtube.com/results" method="get" target="_blank" >
                <input name="search_query" type="text" maxlength="128" />
                <select name="search_type">
                <option value="">Videos</option>
                <option value="search_users">Channels</option>
                </select>
                <input type="submit" value="Search" />
                </form>
                """
            )

    #Building out the Contact Page
    if page_selection == "Contact Us":
        st.info("Let us get in touch for all your ML needs")
        firstname = st.text_input("Enter your Name", "Type Here Please...")
        lastname = st.text_input("Enter your Last Name", "Type Here Please..")
        contactdetails = st.text_input("Enter your contact details here", "Type Here Please...")
        message = st.text_area("Tell us about your company's Data Science needs", "Type here Please..")
  
        if st.button("Submit"):
            result = message.title()
            st.success(result)

    if page_selection == "About Team 2":
        st.subheader("TEAM 2 is a group of five Data Scientists from EDSA")
        st.subheader("Samuel Aina")
        st.image('resources/imgs/samuel.PNG')
        st.subheader(" ")
        st.subheader("Visit our Contact Page and let us get in touch!")


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
