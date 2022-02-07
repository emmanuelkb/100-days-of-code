from data import question_data
from question_model import Question
from quiz_brain import  QuizBrain


question_list = []

for _ in question_data:
    question = Question(_['question'],_['correct_answer'])
    question_list.append(question)

questions = QuizBrain(question_list)
while questions.still_has_questions():
    questions.next_question()

print("\n\nQuiz Completed")
print(f"Your final score was {questions.score} out of {len(questions.question_list)}")


