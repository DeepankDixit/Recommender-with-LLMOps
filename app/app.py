import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommended")

load_dotenv()
#loading env vars here so that when this is dockerized, env variables are loaded as only the app/ folder goes in docker

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences eg. : Light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you...")
    response = pipeline.recommend(query=query)
    st.markdown("### Recommendations")
    st.write(response)

