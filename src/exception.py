import sys as _sys

#from joblib.test.test_my_exceptions import CustomException2
from src.logger import logging

#whenever error occurs , we can push our own custom msg.
#error detail present inside _sys.
#sys contains info about exception occuring in the program. 
def error_message_detail(error,error_detail:_sys):
    #error_details is of type _sys. 

    _,_,exc_tb = error_detail.exc_info()

    #exc_info() returns the tuple whose three items are the class, object, and traceback for the exception. 
    #we need only exc_tb(traceback for the exception)

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error) )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:_sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#         #the value of __name__ varies depending on how our Python code is executed
#     try:
#         a= 1/0
#     except Exception as e :
#         logging.info("divided by zero error")
#         raise CustomException(e,_sys)



        
