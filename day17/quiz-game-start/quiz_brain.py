#create a class
class QuizBrain:
    
    #initialize the ATTRIBUTES
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list  = q_list
        
        self.score = 0
    
    # initialize the methods   
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}:{current_question.text} (True/False) ")
        self.check_ans(user_ans, current_question.answer)
        
    def still_has_questions(self):
        #short hand method of returning true.
        return self.q_number <len(self.q_list)
    
        #this is another way of doing it
        # if self.question_number > len(self.question_list):
        #     return True
        # else:
        #     False
        
    def check_ans(self, user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you got it right")
            self.score += 1
        else:
            print("you got it wrong")
        
        print(f"the correct answer is {correct_ans}")
        print(f"your current score is {self.score} / {self.q_number} \n")
        
        