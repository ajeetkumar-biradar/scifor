class Quiz:
    def __init__(self):
        self.questions = [
            "What is the capital of india?",
            "How many time RCB won the cup in IPL?",
            "Who wrote Nation Anthem?"
        ]
        self.answers = [
            ["Delhi", "Mumbai", "Chennai"],
            ["One", "Two", "Three"],
            ["Tagore", "Kuvempu", "Bendre"]
        ]
        self.correct_answers = [0, 0, 0]
        self.score = 0

    def run_quiz(self):
        print("Welcome to the Quiz!")
        for i in range(len(self.questions)):
            print("\nQuestion", i + 1)
            print(self.questions[i])
            for j, answer in enumerate(self.answers[i]):
                print(f"{j + 1}. {answer}")
            user_answer = int(input("Your answer (1, 2, or 3): ")) - 1
            if user_answer == self.correct_answers[i]:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        print("\nQuiz completed!")
        print("Your score:", self.score, "/", len(self.questions))


quiz = Quiz()
quiz.run_quiz()
