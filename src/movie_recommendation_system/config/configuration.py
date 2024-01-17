from pathlib import Path
from movie_recommendation_system.constants import *
from movie_recommendation_system.utils.common import read_yaml,create_directories
from movie_recommendation_system.entity.config_entity import (DataIngestionConfig,
                                                            DataTransformationConfig)

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        temp_config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir = temp_config.root_dir,
            source = temp_config.source,
            local_data_file = temp_config.local_data_file,
            unzip_dir = temp_config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        temp_config = self.config.data_transformation

        data_transformation_config = DataTransformationConfig(
            root_dir = temp_config.root_dir,
            movies_data = temp_config.movies_data,
            credits_data = temp_config.credits_data,
            cleaned_data_path = temp_config.cleaned_data_path
        )
        return data_transformation_config