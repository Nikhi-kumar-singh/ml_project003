import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%d_%m_%y_%Hh_%Mm_%Ss')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)


os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)



if __name__=="__main__":
    print(f"log file : {LOG_FILE}")
    print(logs_path)
    print(LOG_FILE_PATH)