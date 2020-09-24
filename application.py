from flask import Flask
import json
from data import intro_list, money_items, win_message, lose_message
from flask_cors import CORS, cross_origin


application = app = Flask(__name__) 
cors = CORS(app)


@app.route("/intro")    
def getIntroMsg():
    return json.dumps(intro_list)


@app.route("/questions")    
def getQuestionDict():
    return json.dumps(money_items)



@app.route("/answers/<input>", methods=['GET', 'POST']) 
def getAnswers(input, x):
    uppercase = False
    compare = money_items[x]
    if (input.__contains__('$')):
        uppercase = True
    if (input.__contains__(compare['correct_num']) and input.contains(compare['correct_scale'])): 
        point = 1
    else:
        point = 0      
    answer_pattern = {"status": ["OK", 200], "uppercase": uppercase, "points": point, "question": x }
    return answer_pattern
    



@app.route("/closing/<score>")
def getClosing(score):
    if score >= 3:
        return win_message
    else:
        return lose_message



if __name__ == "__main__" :
    app.run(debug=True)

