
#INTRO MESSAGES
intro_list = ['''The goal of this mini-game is to test your knowledge about money trivia. You will receive 2 points for every correct answer.\n\

Your tools are below: a bar to type your response,  a button to submit your answer, and a button to request a hint for a total of 3 times.  ''',

'''The questions are timed so have your favorite search engines ready. You must send an answer before time runs out.\n\

You will receive instant feedback.  ''',

"There is no penalty for guessing or getting a wrong answer, so put whatever you think.  ",

'''Please type your answers using numbers when writing numeric values.

Remember to have fun!

Are you ready?

Lets Go!!!!'''
]


#QUESTIONS DICTIONARY LIST
money_items = [
    { 'id'         :   0,
      'question'   :   'What is the net worth of the richest man in the world?',
       'answer'    :   '113 billion',
        'hint'     :   'The answer is in the order of billions to the triple digits'},
    
    { 'id'         :    1, 
      'question'   :   'What is Warren Buffet\'s net worth?',
       'answer'    :   '67 billion ',
       'hint'      :   'Its half...the greater half of the richest man\'s income'},

    { 'id'         :    2,
      'question'   :   'How much was Bloomberg\'s salary while working as mayor of NYC in 2009?', 
      'answer'     :   '1 dollar',
      'hint'       :   'It\'s a very small number'},

    { 'id'         :   3,
      'question'   :   'What is the average NFL player salary per season?', 
       'answer'    :   '2.7 million',
        'hint'     :   'Well ... they are definitely millionaires'},

    {  'id'        :   4,
       'question'  :   'How much does an average software engineer in Silicon Valley earn   in a year?',
        'answer'   :   '101,876 dollars',
        'hint'     :    'It\'s six figures, but maybe not as high as you think'}
]


#USER SUCCESS
win_message = {" You are a money mogul and you have won this mini-game! \n\ Your prize is... a lifetime of financial success!!!  Check out this article for more info https://www.forbes.com/billionaires/"}

lose_message = {"However you are a winner in real life and that is all that matters!\n\ May you enjoy a lifetime of financial success!! Check out this article for more info https://www.forbes.com/billionaires/"}
  
