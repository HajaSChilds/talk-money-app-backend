
#INTRO MESSAGES
intro_list = ['''The goal of this mini-game is to test your money trivia knowledge.

Use the white bar to type your response,  the pink button to submit your answer, and the blue button to request a hint. You have a total of 3 hints for the game.  ''',

'''The questions are timed so be ready. You must send an answer before time runs out.''',

'''You will receive 1 point for each correct answer. here is no penalty for putting a wrong answer, so feel free to estimate.  ''',

'''Rules: Type answers using numbers and scale when writing numeric values, i.e - 2 million or 2,000,000''', 

'''Remember to have fun!

Are you ready?

Lets Go!!!!'''
]


#QUESTIONS DICTIONARY LIST
money_items = [
    { 'id'         :   0,
      'question'   :   'What is the net worth of the richest man in the world?',
       'answer'    :   '113 billion',
        'hint'     :   'The answer is in the order of billions to the triple digits',
    'correct_num'  :    [100,200],
    'correct_scale':    ['billion', ',000,000,000']},
    
    { 'id'         :    1, 
      'question'   :   'What is Warren Buffet\'s net worth?',
       'answer'    :   '67 billion ',
       'hint'      :   'Its half...the greater half of the richest man\'s income',
      'correct_num':    [30,80],
    'correct_scale':    ['billion', ',000,000,000']},

    { 'id'         :    2,
      'question'   :   'How much was Bloomberg\'s salary while working as mayor of NYC in 2009?', 
      'answer'     :   '1 dollar',
      'hint'       :   'It\'s a very small number',
    'correct_num'  :    [1,10],
    'correct_scale':    ['dollar', '.00']},

    { 'id'         :   3,
      'question'   :   'What is the average NFL player salary per season?', 
       'answer'    :   '2.7 million',
        'hint'     :   'Well ... they are definitely millionaires',
    'correct_num'  :    [1,5],
    'correct_scale':    ['million', ',000,000']},

    {  'id'        :   4,
       'question'  :   'How much does an average software engineer in Silicon Valley earn   in a year?',
        'answer'   :   '101,876 dollars',
        'hint'     :    'It\'s six figures, but maybe not as high as you think',
      'correct_num':    [80, 200],
    'correct_scale':    ['hundred-thousand', '00,000']}
]


#USER SUCCESS
win_message = {" You are a money mogul and you have won this mini-game! \n\ Your prize is... a lifetime of financial success!!!  Check out this article for more info https://www.forbes.com/billionaires/"}

lose_message = {"However you are a winner in real life and that is all that matters!\n\ May you enjoy a lifetime of financial success!! Check out this article for more info https://www.forbes.com/billionaires/"}
  
