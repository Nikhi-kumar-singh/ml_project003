# from Network_Security.logger.logger import logging 

import os
import sys




class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "error occured in python scripy name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name,
            self.lineno,
            str(self.error_message)
        )

        
    

class ShowException(Exception):
    def __init__(self,error_detail:sys):
        self.current_exceptions=error_detail._current_exceptions()
        self.exception=error_detail.exception()


    def __str__(self):
        return "current exceptions : [{0}],\n exception : [{1}]".format(
            self.current_exceptions,
            self.exception
        ) 



# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info(f"exception is being raised")
#         raise NetworkSecurityException(e,sys)
#         raise ShowException(sys)