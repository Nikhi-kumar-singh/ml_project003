
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.entity.artifact_entity import ClassificationMetricArtifact

from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score
)




def get_classification_score(y_true,y_pred)->ClassificationMetricArtifact:
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_precision_score=precision_score(y_true,y_pred)
        model_recall_score=recall_score(y_true,y_pred)

        classification_metric_artifact_score=ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score=model_recall_score
        )

        return classification_metric_artifact_score
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)