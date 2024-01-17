import sys
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.utils.logger import logger
from movie_recommendation_system.config.configuration import ConfigurationManager
from movie_recommendation_system.components.comp_02_data_transformation import DataTransformation


class DataTransformationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.initiate_data_transformation()
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