from question_model import Queastion
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Queastion(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
