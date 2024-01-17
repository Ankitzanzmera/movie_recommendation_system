import sys
from movie_recommendation_system.utils.logger import logger
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.pipelines.pipeline_01_data_ingestion import DataIngestionPipeline
from movie_recommendation_system.pipelines.pipeline_02_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*70)
    except Exception as e:
        raise CustomException(e,sys)

STAGE_NAME = "Data Transformation"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*70)
    except Exception as e:
        raise CustomException(e,sys)