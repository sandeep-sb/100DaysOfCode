from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in range(0, len(question_data)):
    question_text = question_data[question].get("question")
    question_answer = question_data[question].get("correct_answer")
    question = Question(text=question_text, answer=question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_data)}")