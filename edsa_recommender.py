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
    page_options = ["Home","Recommender System","Interactive Movie Recommender","Data Analysis & Insights","Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == "Home":
        st.image('resources/imgs/Home.png', width=900)


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
 
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
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
                        st.write('1st')
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                        st.write('here')
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------
    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Data Analysis & Insights":

        from bokeh.io import show, output_notebook
        from bokeh.plotting import figure   

        st.title("Data Analysis & Insights")
        st.subheader('Understanding the data')
        st.write("Below we explore the data through visualisation to better understand the industry it represents and how it has changed over the years")

        st.warning('This dataset contains over 48 000 unique movies with release dates all the way from 1874, around the time when motion pictures were first invented, to 2019 when Avengers: Infinity War part II rocked the big screen')
        
        # Rating distribution
        st.write('Although ratings were only created/collected from 1995 to 2019, almost every movie in the dataset has numerous user ratings. The graph below illustrated the trend of high average ratings in general with an overall average rating of 3.5')
        st.image('resources/imgs/ratings_dist.png', width=900)

        # Number of ratings vs ratings scatterplot - more ratings = higher average rating (trend)
        st.write('The plot below illustrates a key trend in the film industry: The more people that view a movie the higher probability it has of having a high average rating. This observation is a key driving point behind marketing strategies in the film industry worldwide')
        st.image('resources/imgs/ratings_scatter.png')

        # Lineplot of movies release from 1874 - 2019
        st.write('The following line graph visualises the trend in number of movies released per year since the first motion pictures were released around 1874. It is important to note that this dataset does not contain every movie ever released (and heavily favours US-released movies), meaning that even though the trend it exposes exists one cannot read off values for any specific year(s) accurately.')
        st.write("The dataset also doesn't contain many movies after 2016, which should not be be interpreted as a reduction in releases around that time.")
        st.image('resources/imgs/movies_per_year.png', width=1000)

        # Wordcloud of most prominent release years
        st.write('This word-cloud depicts the years with singularly the most recorded releases in this dataset.')
        st.image('resources/imgs/wordcloud_year.png', width=700)

        # Genre wordcloud
        st.write("This wordcloud similarly depicts the most prominent genres represented in this dataset. Comedy, Drama, Romance, and Sci-Fi dominate with Action, Thriller, Crime, and Drama following closely.")
        st.image('resources/imgs/wordcloud_genre.png', width=700)

        # Ratings by Day of Week
        st.markdown("The following graph shows the trends in day-of-week rating of movies in this dataset. Sundays and Saturdays are understandably most prominent, though the step-wise decrease from Sunday to Friday indicates that the overall rating trend here might simply be an artefact of the manner in which the dataset was constructed (everybody knows Thursdays and Fridays are prime movie nights :wink:).")
        st.image('resources/imgs/ratings_DOW.png', width=700)

        # Movie duration distribution
        st.write("The violin-plot below visualises the distribution in movie duration in the dataset, clearly showing that, with few outliers, movie duration is on average around 100 minutes.")
        st.image('resources/imgs/movie_duration.png', width=600)

        st.subheader("That wraps up our dive into the dataset! For more in-dept analytics get in touch with us though the 'Contact Us' page.")


    if page_selection == "Interactive Movie Recommender":

        # Setting up background image:
        st.image('resources/imgs/background.jpg', width=800)

        # Page title & intro
        st.title("Interactive Movie Recommender")
        st.subheader("Don't trust the system! Find your own movies here.")
        st.info("Below is a more interactive movie recommender. Set your release date (year) preference with the two year sliders and select any combination of your preferred genres. On the table that displays your recommendations, click on the 'year' column title to sort the recommendations by release year. Copy and paste the title of any films that catch your eye into the search bar below the table to search youtube for its trailer")

        # Container for year/genre filtered DF
        with st.beta_container():
            # Load movies.csv dataframe:
            movies_df = pd.read_csv('resources/data/movies.csv', index_col='movieId')

            # Year selection
            st.subheader('Enter your preferred release-year range')
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



            # Display filtered DF
            st.dataframe(movies_df)

        with st.beta_container():
            st.image('resources/imgs/Youtube_logo.png', width=300)
            st.subheader('Search YouTube')
            st.info('Copy and paste movie titles that catch your fancy below to search youtube!')
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

        st.subheader("We are Team 2, a group of young data scientists from the Explore Data Science Academy, Johannesburg.")

        with st.beta_container():
            st.subheader("Samuel Aina")
            st.text('sammykola@yahoo.com')

            st.subheader("Jacques Carstens")
            st.text('carstensjacques3@gmail.com')

            st.subheader("Mokgadi Maake")
            st.text('mj.maakekai@gmail.com')

            st.subheader("Sandile Mkhabela")
            st.text('saintsandile01@gmail.com')


        st.info("Get in touch with us for all your ML needs")
        firstname = st.text_input("Enter your Name")
        lastname = st.text_input("Enter your Last Name")
        contactdetails = st.text_input("Enter your contact details here")
        message = st.text_area("Tell us about your company's Data Science needs")
  
        if st.button("Submit"):
            result = message.title()
            st.success("Thank you, we'll be in touch!")


if __name__ == '__main__':
    main()