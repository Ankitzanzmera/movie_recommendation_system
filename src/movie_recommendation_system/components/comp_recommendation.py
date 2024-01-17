import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download("wordnet")
nltk.download("stopwords")
import pandas as pd
from tqdm import tqdm
import pickle
from movie_recommendation_system.constants import *
from movie_recommendation_system.utils.common import read_yaml,create_directories
from movie_recommendation_system.utils.exception import CustomException
from movie_recommendation_system.utils.logger import logger
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Prediction:
    def __init__(self,config_filepath = CONFIG_FILEPATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.prediction.root_dir])

        self.lemmatizer = WordNetLemmatizer()
        self.tfidf = TfidfVectorizer(max_features = 2000)

    def __lemmatizing__(self,text):
        words = []

        for word in tqdm(text.split()):
            if not word in stopwords.words("english"):
                lemmatized_word = self.lemmatizer.lemmatize(word)
                words.append(lemmatized_word)
        corpus = " ".join(words)
        return corpus

    def __vectorizer__(self):
        self.vectors = self.tfidf.fit_transform(self.df['tags']).toarray()
        print(self.vectors.shape)

    def __similarity__(self):
        similarity = cosine_similarity(self.vectors)
        pickle.dump(similarity,open(self.config.prediction.similarity_path,"wb"))
        print(similarity)


    def initiate_prediction(self):

        self.df = pd.read_csv(self.config.data_transformation.cleaned_data_path)
        self.df['tags'] = self.df['tags'].apply(self.__lemmatizing__)
        self.__vectorizer__()
        self.__similarity__()
        pickle.dump(self.df.to_dict(),open(self.config.prediction.movie_dict,"wb"))

