# 🧠 ML Project 003 - End-to-End Machine Learning Pipeline

An end-to-end machine learning project with a production-grade pipeline designed for training, evaluating, and deploying scalable ML models. This project is modular, reproducible, and aligned with best MLOps practices.

---

## 📁 Project Structure
# to create the project structure
# run command - python create_tree.py

ml_project003/
├── Dockerfile
├── Network_Data
│   ├── __init__.py
│   ├── cluster_data.txt
│   ├── get_local_data.py
│   ├── get_remote_data.py
│   ├── phisingData.csv
│   ├── push_data.py
│   └── test_mongo.py
├── Network_Security
│   ├── __init__.py
│   ├── cloud
│   │   ├── __init__.py
│   │   └── s3_syncer.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── data_validation.py
│   │   └── model_trainer.py
│   ├── constants
│   │   ├── __init__.py
│   │   └── training_pipeline
│   │       ├── __init__.py
│   ├── entity
│   │   ├── __init__.py
│   │   ├── artifact_entity.py
│   │   └── config_entity.py
│   ├── exception
│   │   ├── __init__.py
│   │   └── exception.py
│   ├── logger
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── batch_prediction.py
│   │   └── training_pipeline.py
│   └── utils
│       ├── main_utils
│       │   ├── __init__.py
│       │   └── utils.py
│       └── ml_utils
│           ├── __init__.py
│           ├── metric
│           └── model
├── Network_Security.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
├── README.md
├── app.py
├── create_tree.py
├── data_schema
│   └── schema.yaml
├── final_model
│   ├── model.pkl
│   └── preprocessor.pkl
├── installed_packages.txt
├── instructions.txt
├── main.py
├── notebooks
│   └── __init__.py
├── requirements.txt
├── setup.py
├── templates
│   └── table.html
└── valid_data
    ├── input.csv
    └── output.csv
                 # Generated artifacts (output files)

