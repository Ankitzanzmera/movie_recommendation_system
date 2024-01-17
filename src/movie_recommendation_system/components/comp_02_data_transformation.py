import os,sys
import ast
import pandas as pd
from movie_recommendation_system.utils.logger import logger
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.entity.config_entity import DataTransformationConfig
from movie_recommendation_system.utils.common import create_directories

class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config = config
        create_directories([self.config.root_dir])

    @property
    def __read_data__(self):
        movies = pd.read_csv(self.config.movies_data)
        credits = pd.read_csv(self.config.credits_data)
        self.dataset = movies.merge(credits,on = "title") 

    @property
    def __rm_unnecessary_cols(self):
        remove_cols = ['id',"budget","homepage",'original_language','original_title','popularity','production_companies','production_countries','release_date','revenue','runtime', 'spoken_languages', 'status', 'tagline','vote_average', 'vote_count']
        self.dataset.drop(remove_cols,axis = 1,inplace= True)
        self.dataset.dropna(inplace = True)
        self.dataset.drop_duplicates(inplace=True)

    def __string_to_list__(self,text):
        text_list = []
        for i in ast.literal_eval(text):
            name = i['name'].replace(" ","")
            text_list.append(name)
        return text_list

    def __top_three_casts__(self,text):
        casts = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter != 3:
                name = i['name'].replace(" ","")
                casts.append(name)
                counter += 1
            else:
                break
        return casts

    def __fetch_director__(self,text):
        director = []
        for i in ast.literal_eval(text):
            if i['job'] == "Director":
                name = i['name'].replace(" ","")
                director.append(name)
                break
        return director
    
    def __prepare_final_dataset__(self):
        self.dataset['tags'] = self.dataset['overview'] + self.dataset['genres'] + self.dataset['keywords'] + self.dataset['cast'] + self.dataset['crew']
        final_df = self.dataset[['movie_id','title','tags']]
        final_df['tags'] = final_df['tags'].apply(lambda x: " ".join(x))
        final_df['tags'] = final_df['tags'].apply(lambda x: x.lower())
        final_df.to_csv(self.config.cleaned_data_path,index = False)

    def initiate_data_transformation(self):
        try:
            self.__read_data__
            logger.info("Read all the data")

            self.__rm_unnecessary_cols
            logger.info("Removed All the Unnecessary cols")
            
            self.dataset['genres'] = self.dataset['genres'].apply(self.__string_to_list__)
            self.dataset['keywords'] = self.dataset['keywords'].apply(self.__string_to_list__)
            self.dataset['cast'] = self.dataset['cast'].apply(self.__top_three_casts__)
            self.dataset['crew'] = self.dataset['crew'].apply(self.__fetch_director__)
            self.dataset['overview'] = self.dataset['overview'].apply(lambda x: x.split())
            logger.info("Applied Some Transformation on columns")
            
            self.__prepare_final_dataset__()
            logger.info("Stored Cleaned Data")

        except Exception as e:
            raise CustomException(e,sys)


