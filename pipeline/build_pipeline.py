from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

"""
This pipeline is used to build the vectorstore i.e. Training pipeline
"""

def main():
    try:
        logger.info("Starting to build pipeline...")

        loader = AnimeDataLoader(original_csv=r"data\anime_with_synopsis.csv", 
                                 processed_csv=r"data\anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("Data loaded and processed")

        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built successfully")

        logger.info("Pipeline built successfully")

    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("Error during pipeline initialization", e)
    
if __name__=="__main__":
    main()
    #means this main() will only get executed when someone runs this file as "python build_pipeline.py"