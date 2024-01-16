import os,sys
import gdown
from zipfile import ZipFile
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.utils.logger import logger
from movie_recommendation_system.entity.config_entity import DataIngestionConfig
from movie_recommendation_system.utils.common import create_directories

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config
        create_directories([self.config.root_dir])

    @property
    def __download_file__(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                gdown.download(self.config.source,self.config.local_data_file)
                logger.info("Zip file Downloaded Successfully")
            else:
                logger.info("Zip file Already Downloaded")
        except Exception as e:
            raise CustomException(e,sys)

    @property
    def __unzip_data___(self):
        try:
            if not os.path.exists(self.config.unzip_dir):
                with ZipFile(self.config.local_data_file,"r") as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                logger.info("Zip file is Extracted")
            else:
                logger.info("Zip file is already Extracted")
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):

        self.__download_file__
        self.__unzip_data___
