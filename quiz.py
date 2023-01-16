question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class A:
    count = 0

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def function(self, i):
        print(self.question)
        candidateanswer = input("Enter your answer (True/False) ")
        if str(candidateanswer).lower() == self.answer.lower():
            A.count += 1
            print(f"Answer was correct, score is {A.count} out of {i}")
            print()
        else:
            print(f"The answer was wrong, The correct answer was {self.answer}, score was {A.count} out of {i}")
            print()


for i in range(len(question_data)):
    a = A(question_data[i]['text'], question_data[i]['answer'])
    a.function(i + 1)
else:
    print("You have completed the quiz")
    print(f"Your final score was {A.count}/{i+1}")