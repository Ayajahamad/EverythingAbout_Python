import logging
from datetime import datetime

import psycopg2

conn = psycopg2.connect(
    host="192.168.2.12",
    database="test",
    user="senscio",
    password="Agile2022#"
)

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger()

class AboutLogging:
    # Define a log message
    def log_start_operation(self,operation_name):
        logger.info("="*50 + f"Begin: {operation_name}: " + str(datetime.now()) + "="*50)
    
    
    def Log_messages_at_various_levels(self):
        # Log messages at various levels
        logger.debug("This is a debug message.")
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")
        logger.critical("This is a critical message.")
        
    def Example_Log_with_insert_employees(self):
        try:
            logger.info("=========================================================Begin: insert_employees: " + str(
                datetime.now()) + " ==============================================================================================================")
            cursor = conn.cursor()
        
            dlt_query = "delete from EmpTask"
            cursor.execute(dlt_query)

            lst = []
            query = """select employee_id,"name" from public.emp1"""
            cursor.execute(query)
            data = cursor.fetchall()
            # print(data)
            for i in data:
                lst+=[i]
            
            print(lst)
        
            query_Insert = """insert into EmpTask(id,name) values"""
            args = ','.join(cursor.mogrify("(%s,%s)",i).decode('utf-8') for i in data)
            # cursor.execute(query_Insert+args)
        
            conn.commit()

            print("Records inserted successfully.")
            
            logger.info("Table: public.EmpTask;Number of Records: " + str(len(lst)))
            
            logger.info("=========================================================End: insert_employees: " + str(
                datetime.now()) + " ==============================================================================================================")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


if __name__=='__main__':
    obj = AboutLogging()
    
    # Log the start of an operation
    # obj.log_start_operation('insert_providers')
    
    # Log messages
    # obj.Log_messages_at_various_levels()
    
    # Inserting the emp table with log message
    obj.Example_Log_with_insert_employees()
    

"""
In Python, logging is a standard way to track and record messages from your code. Logs are essential 
for monitoring applications, debugging issues, and understanding the flow of execution. The Python 
logging module provides a flexible framework for emitting log messages from Python programs.

The Basics of Logging
What is Logging?
Logging is the process of recording events, actions, or messages from a program as it runs. This can 
include information about:

Errors: Issues that need immediate attention.
Warnings: Potential problems or important conditions.
Info: General operational messages that track the application's progress.
Debug: Detailed information useful for diagnosing problems.
"""



