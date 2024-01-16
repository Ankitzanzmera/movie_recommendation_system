import os,sys
import logging
from datetime import datetime

dirname = f"{datetime.now().strftime('%d_%m_%y')}"
dir_path = os.path.join(os.getcwd(),"logs",dirname)
os.makedirs(dir_path, exist_ok= True)

file_name = f"{datetime.now().strftime('%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(dir_path,file_name)

logging.basicConfig(
    level = logging.INFO,
    format = " [%(asctime)s] - %(module)s - %(lineno)d - %(message)s",
    handlers = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE_PATH)
    ]
)

logger = logging.getLogger("movie_recommendation_system_logger")