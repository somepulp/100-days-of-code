# we want to bring in question data, and store it in a list of Question objects
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] 
for dict in question_data:
    question_text = dict['question']
    question_answer = dict['correct_answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_list=question_bank) 
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")