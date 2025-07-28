# 🧠 ML Project 003 - End-to-End Machine Learning Pipeline

This repository contains a complete **End-to-End Machine Learning Pipeline** project that automates the ML lifecycle, including data ingestion, validation, transformation, model training, evaluation, and deployment.

This project is modular, reproducible, scalable, and production-ready. It follows the best MLOps practices and is designed to be extended for various network security use-cases.

---

### To start the app, write the commands below

#### 1. Set the virtual environment
**python -m venv myvenv**

#### 2. Activate the virtual environment
**source myvenv/Scripts/activate**

#### 3. Install the dependencies
**pip install -r requirements.txt**

#### 4. Set up your file system locations
- Set up **.env** file  
- Set up **Network_Security/training_pipeline/__init__.py** taking inspiration from the example.py file

#### 5(a). Run the **app.py** file
```bash
uvicorn app:app
```

5(b).in case of ***developement phase** and want to run the program
```bash
uvicorn app:app --reload
```

---

## 📁 Project Structure
##### to create the tree of the project run command -
```bash
python create_tree.py
```

```

ml_project003/
├── Dockerfile                        # Docker configuration for containerization
├── Network_Data/                     # Scripts related to data collection and ingestion
│   ├── cluster_data.txt              # Sample cluster data
│   ├── get_local_data.py             # Load local dataset
│   ├── get_remote_data.py            # Load dataset from remote
│   ├── phisingData.csv               # CSV data file
│   ├── push_data.py                  # Push data to database
│   └── test_mongo.py                 # MongoDB test connection
├── Network_Security/                 # Core package
│   ├── cloud/                        # Cloud storage interface
│   │   └── s3_syncer.py              # AWS S3 syncing script
│   ├── components/                   # Pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── data_validation.py
│   │   └── model_trainer.py
│   ├── constants/                    # Configuration constants
│   ├── entity/                       # Entity definitions for config/artifact
│   ├── exception/                    # Custom exception handling
│   ├── logger/                       # Logging utilities
│   ├── pipeline/                     # Pipeline entry scripts
│   │   ├── training_pipeline.py
│   │   └── batch_prediction.py
│   └── utils/                        # Utility functions
│       ├── main_utils/
│       └── ml_utils/
├── final_model/                      # Final trained model artifacts
│   ├── model.pkl
│   └── preprocessor.pkl
├── data_schema/                      # Input schema
│   └── schema.yaml
├── valid_data/                       # Sample valid test data
│   ├── input.csv
│   └── output.csv
├── installed_packages.txt            # Conda or pip list snapshot
├── create_tree.py                    # Script to create folder structure
├── app.py                            # Flask API for model prediction
├── main.py                           # Main script to run pipeline
├── requirements.txt                  # Python dependencies
├── setup.py                          # Project packaging
├── README.md                         # This documentation
├── instructions.txt                  # Developer instructions
└── templates/
    └── table.html                    # HTML template for API response

```

---


## 📊 Project Class Diagram

```
                            +----------------------------+
                            |        main.py             |
                            |----------------------------|
                            | - Triggers the pipeline    |
                            +-------------+--------------+
                                          |
                                          v
                            +-------------+--------------+
                            |    TrainingPipeline        |
                            |----------------------------|
                            | - start_data_ingestion()   |
                            | - start_data_validation()  |
                            | - start_data_transformation()|
                            | - start_model_trainer()    |
                            +-------------+--------------+
                                          |
        +------------------+--------------+---------------------+------------------+
        |                  |                                    |                  |
        v                  v                                    v                  v
+----------------+  +----------------------+        +----------------------+  +-----------------------+
| DataIngestion  |  | DataValidation       |        | DataTransformation   |  | ModelTrainer          |
|----------------|  |----------------------|        |----------------------|  |------------------------|
| +__init__()    |  | +__init__()          |        | +__init__()          |  | +__init__()            |
| +initiate()    |  | +validate()          |        | +transform()         |  | +train()               |
+-------+--------+  +----------+-----------+        +----------+-----------+  +-----------+-----------+
        |                     |                               |                              |
        v                     v                               v                              v
+---------------------+  +------------------------+  +------------------------+     +----------------------------+
| DataIngestionConfig |  | DataValidationConfig   |  | DataTransformationConfig|     | ModelTrainerConfig        |
+---------------------+  +------------------------+  +------------------------+     +----------------------------+
        |                     |                               |                              |
        v                     v                               v                              v
+---------------------+  +-------------------------+ +-------------------------+     +----------------------------+
| DataIngestionArtifact| | DataValidationArtifact  | | DataTransformationArtifact|    | ModelTrainerArtifact       |
+---------------------+  +-------------------------+ +-------------------------+     +----------------------------+

```


## Sequence Diagram


```

User              TrainingPipeline         ConfigurationManager        DataIngestion      DataValidation     DataTransformation     ModelTrainer     ModelEvaluation     ModelPusher
 |                        |                         |                          |                   |                       |                  |                   | 
 |-- run_pipeline() ----->|                         |                          |                   |                       |                  |                   |
 |                        |--load configurations -->|                          |                   |                       |                  |                   |
 |                        |                         |---> data_ingestion_config                     |                       |                  |                   |
 |                        |                         |---> data_validation_config                    |                       |                  |                   |
 |                        |                         |---> data_transformation_config                |                       |                  |                   |
 |                        |                         |---> model_trainer_config                      |                       |                  |                   |
 |                        |                         |---> model_evaluation_config                   |                       |                  |                   |
 |                        |                         |---> model_pusher_config                       |                       |                  |                   |
 |                        |------------------------>|                          |                   |                       |                  |                   |
 |                        |                         |-- init ingestion config-->|                   |                       |                  |                   |
 |                        |                         |                          |-- download data -->|                       |                  |                   |
 |                        |                         |                          |-- return artifact--|                       |                  |                   |
 |                        |----------------------------->|                     |-- validate schema -->|                       |                  |                   |
 |                        |                               |                   |-- return artifact---|                       |                  |                   |
 |                        |--------------------------------------->|           |-- transform data --->|                       |                  |                   |
 |                        |                                       |           |-- return artifact-----|                       |                  |                   |
 |                        |--------------------------------------------------->|                     |-- train model ------->|                  |                   |
 |                        |                                                  |                     |-- return artifact------|                  |                   |
 |                        |----------------------------------------------------------------------->|                     |-- evaluate model ->|                   |
 |                        |                                                                      |                     |-- return artifact---|                   |
 |                        |--------------------------------------------------------------------------------------------------->| push model ------>|
 |                        |                                                                                                  |-- return artifact--|
 |<---------------------- done                                                                                                               


```

- Name: Nikhil Kumar  
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/nikhil-kumar-5b1072293/)  
- Email: nikhilkumarsingh5872@gmail.com

