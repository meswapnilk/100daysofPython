#TODO asking the questions
#TODO checking if answer was correct
#TODO checking if we are at the end of the quiz
class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1 }. {current_question.text} (True/False)? ")
        self.question_number += 1
        if self.check_answer(user_answer, current_question.answer):
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong!")
        print(f"The correct answer is {current_question.answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()
    
    def final_score(self):
        print("You have completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")
