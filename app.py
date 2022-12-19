from flask import Flask
import sys
from Housing.logger import logging
from Housing.exception import Housingexception

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom error message")
    except Exception as e:
        housing = Housingexception(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "Starting Machine learning Project"


if __name__=="__main__":
    app.run(debug=True)