import sys
from movie_recommendation_system.components.comp_recommendation import Prediction
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.utils.logger import logger

class PredictionPipeline:
    def main(self):
        try:
            obj = Prediction()
            obj.initiate_prediction()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = "vectorizing "
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PredictionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*70)
    except Exception as e:
        raise CustomException(e,sys)