import sys
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.utils.logger import logger
from movie_recommendation_system.config.configuration import ConfigurationManager
from movie_recommendation_system.components.comp_01_data_ingestion import DataIngestion

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingesion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingesion_config)
            data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)


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
    