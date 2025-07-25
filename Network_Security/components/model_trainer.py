import os,sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.entity.artifact_entity import (
    DataTransformationArtifact,
    ClassificationMetricArtifact,
    ModelTrainerArtifact
)
from Network_Security.entity.config_entity import (
    ModelTrainerConfig
)
from Network_Security.utils.ml_utils.model.estimator import NetworkModel


from Network_Security.utils.main_utils.utils import (
    save_numpy_array_data,
    load_numpy_array_data,
    save_object,
    load_object,
    evaluate_models
)
from Network_Security.utils.ml_utils.model.estimator import NetworkModel

from Network_Security.utils.ml_utils.metric.classification_metric import get_classification_score   


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier 
)



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config:ModelTrainerConfig,
        data_transformation_artifact:DataTransformationArtifact
    ):
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        


    def train_model(
            self,
            x_train,
            y_train,
            x_test,
            y_test
        ):   
        models = {
            "Random Forest": RandomForestClassifier(verbose=1),
            "Gradient Boost": GradientBoostingClassifier(verbose=1),
            "Ada Boost": AdaBoostClassifier(),
            "Decision Tree": DecisionTreeClassifier(),
            "Logistic Regression": LogisticRegression()
        }

        params = {
            "Random Forest": {
                'n_estimators': [100, 200],
                'criterion': ['gini', 'entropy', 'log_loss'],
                'max_depth': [10, 20, 30],
            },
            "Gradient Boost": {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 5, 7],
            },
            "Ada Boost": {
                'n_estimators': [50, 100],
                'learning_rate': [0.01, 0.1, 1]
            },
            "Decision Tree": {
                'criterion': ['gini', 'entropy', 'log_loss'],
                'max_depth': [5, 10, 20]
            },
            "Logistic Regression": {
                'C': [0.01, 0.1, 1, 10],
                'solver': ['lbfgs', 'liblinear']
            }
        }


        model_report:dict=evaluate_models(
            x_train=x_train,
            y_train=y_train,
            x_test=x_test,
            y_test=y_test,
            models=models,
            params=params
        )

        best_model_score=0
        best_model_name=""
        best_model={}

        for model_name,model_data in model_report.items():
            model_score=model_data["score"]

            if model_score > best_model_score : 
                best_model_name=model_name
                best_model_score=model_score
                best_model=model_data["model"]

        logging.info(
            f"best model name : {best_model_name}",
            f"best score : {best_model_score}"
        )


        y_train_pred = best_model.predict(x_train)

        classification_train_metric=get_classification_score(
            y_true =   y_train,
            y_pred = y_train_pred
        )

        y_test_pred=best_model.predict(x_test)

        classification_test_matric=get_classification_score(
            y_true =y_test,
            y_pred=y_test_pred
        )

        preprocessor = load_object(
            file_path=self.data_transformation_artifact.transformed_object_file_path
        )

        model_dir_name=os.path.dirname(self.model_trainer_config.trained_model_file_path)

        os.makedirs(model_dir_name,exist_ok=True)


        network_model_obj=NetworkModel(
            preprocessor=preprocessor,
            model=best_model
        )

        save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=network_model_obj
        )

    #     class ModelTrainerArtifact:
    # train_model_file_path:str
    # train_metric_artifact: ClassificationMetricArtifact
    # test_metric_artifart: ClassificationMetricArtifact

        model_trainer_artifact_obj=ModelTrainerArtifact(
            train_model_file_path=self.model_trainer_config.trained_model_file_path,
            train_metric_artifact=classification_train_metric,
            test_metric_artifact=classification_test_matric
        )


        return model_trainer_artifact_obj
    

        

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path=self.data_transformation_artifact.transformed_train_file_path

            test_file_path=self.data_transformation_artifact.transformed_test_file_path

            train_arr=load_numpy_array_data(train_file_path)

            test_arr = load_numpy_array_data(test_file_path)

            x_train,y_train,x_test,y_test=(
                train_arr[:, : -1],
                train_arr[:, -1],
                test_arr[:, : -1],
                test_arr[:, -1]
            )

            logging.info(
                f"shape of the data for training and testing : \n"
                f"x_train {x_train.shape}",
                f"x_test : {x_test.shape}",
                f"y_train : {y_train.shape}",
                f"y_test : {y_test.shape}"
            )

            model_trainer_artifact_obj=self.train_model(
                x_train,
                y_train,
                x_test,
                y_test
            )

            return model_trainer_artifact_obj

        except Exception as e:
            raise NetworkSecurityException(e,sys)