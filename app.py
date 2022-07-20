import sys
from flask import Flask, app
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("Testing Housing Exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        
    logging.info("Testing Logging module")
    return "Machine Learning End to End project"

if __name__ == "__main__":
    app.run(debug=True)