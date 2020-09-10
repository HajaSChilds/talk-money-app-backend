from flask import Flask
from data import introList

application = app = Flask(__name__) 



@app.route("/intro")    
def getIntroMsg():
    return introList


@app.route("/questions")    
def getQuestionDict():
    pass


@app.route("/closing")
def getClosing():
    pass

print(getIntroMsg())


if __name__ == "__main__" :
    app.run(debug=True)

