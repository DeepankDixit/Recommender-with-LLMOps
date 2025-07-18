from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

"""
This pipeline is used to generate the responses i.e. Prediction/Inference/Recommendation pipeline
"""

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma-db"):
        try:
            logger.info("Initializing recommendation pipeline...")
            
            vectorstore_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir) #empty csv path because we only wanna load the vectorstore builder, not create it
            
            retriever = vectorstore_builder.load_vectorstore().as_retriver()
            
            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Pipeline initialized successfully")
        
        except Exception as e:
            logger.error(f"Failed to initialize pipeline {str(e)}")
            raise CustomException("Error during pipeline initialization", e)
        
    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Received a query {query}")

            recommendation = self.recommender.get_recommendation(query=query)

            logger.info("Recommendation generated successfully")

            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation", e)