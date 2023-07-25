import os 
import sys 
from dataclasses import dataclass

from sklearn.ensemble import (
    RandomForestClassifier )
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
#This module provides a decorator and functions for automatically adding generated special methods such as __init__() and __repr__() to user-defined classes
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class   ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        

    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):
        try:
            logging.info("split training and test input data")
            X_train,y_train,X_test,y_test=(train_array[:,:-1],
                                           train_array[:,-1],
                                           test_array[:,-1],
                                           test_array[:,-1])
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,Y_test = y_test,models=models)

            ## to get best model score from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("no best model found")
            logging.info(f"Best found model on both training and testing dataset ")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            predicted = best_model.predict(X_test)

            r2_square  = r2_score(y_test,predicted)
            return r2_square 
        except:
            pass

