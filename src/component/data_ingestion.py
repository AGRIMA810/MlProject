import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.component.data_transformation import DataTransformation
from src.component.data_transformation import DataTransformationConfig
from src.component.model_trainer import ModelTrainerConfig
from src.component.model_trainer import ModelTrainer


@dataclass
#dataclass is a decorator.
#inside a class, to define class variable we need init function.by using data class we can directly define class variable without init function 
class DataIngestionConfig: #class created 
    train_data_path: str= os.path.join('artifacts',"train.csv")
    #train_data_path is class object with type string. 
    #created artifact folder to save all the files in this path. all the data will be saved in this path...file name is train.csv
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    #raw data is initial data 
    #now the data ingestion config knows where to save the train path,test path  
    #dataIngestionConfig provides all the input things 

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        #this ingestion_config consist of three values. dataIngestionConfig is initialized. when dataIngestion is called - then these three path will be saved inside particular class variable.
         
        #Data Ingestion with Pandas is the process of shifting data from a variety of sources, into the Pandas DataFrame structure.


    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df=pd.read_csv("Notebook\Data\Ulta Skincare Reviews.csv")
            #reading the dataset over here .
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header= True)

            logging.info("Train test split initiated")
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42) #doubt 1 
            #there’s one fixed shuffled dataset for random_state value 42. It means whenever we use 42 as random_state, it’ll return a shuffled dataset.

        

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()








