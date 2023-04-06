class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'{self.question_number}: {current_q.text} (True/False):')
        correct_answer = current_q.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == 'end' or user_answer.lower() == 'off':
            self.still_has_questions = False
        elif user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That is wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}.")
        print("\n")
