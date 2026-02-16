
#import modules 
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


#create a loop to iterate over the question_data
question_bank = []
for question in question_data:
    
    #set variables to store the data from question_data through supplying 'key'
    #value from the question dictionary data.
    q_text = question["text"]
    q_answer = question["answer"]
    
    #Create a Question object from each entry to question_data
    new_q = Question(q_text,q_answer)
    
    #Append each question object to the question_bank
    question_bank.append(new_q)

#ask the user a question
quiz = QuizBrain(question_bank)

#create a loop to keep asking questions if there are still more questions
while quiz.still_has_questions():
    quiz.next_question()

# print(f"you've completed the quiz and your final score is {quiz.score} / {len(quiz.question_list)}")