
#create a class for the QUESTION model
class Question:
    
    def __init__(self,q_text,q_answer):
        
        #create  and initialize the  2 ATTRIBUTES for the class
        self.text = q_text
        self.answer = q_answer

#eg
# new_q = Question("anderson", "crosbie")
# print(new_q.text,new_q.answer)