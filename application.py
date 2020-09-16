from flask import Flask
import json
from data import intro_list, money_items
from flask_cors import CORS, cross_origin


application = app = Flask(__name__) 
cors = CORS(app)


@app.route("/intro")    
def getIntroMsg():
    return json.dumps(intro_list)


@app.route("/questions")    
def getQuestionDict():
    return json.dumps(money_items)

@app.route("/answers") 
def getAnswers():
    pass

@app.route("/closing")
def getClosing():
    pass


if __name__ == "__main__" :
    app.run(debug=True)

