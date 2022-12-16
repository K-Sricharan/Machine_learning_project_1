import os
import sys

class Housingexception(Exception):
    
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)

        

        self.error_message=error_message
    
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys)->str:
        """
        error_message: exception object
        error_detail: object of sys module

        """
        _,_ ,exec_tb = error_details.exc_info()

        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename


        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error_message: [{error_message}]"
        
        return error_message