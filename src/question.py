from random import shuffle

class Question:
    """Basic Question class

    Attributes:
        qtype: A String which indicates the question type
        c_answer: A tuple wich contains the correct answers
        w_answer: A tuple wich contains the incorrect answers
    """
    def __init__(self, sentence, statement, c_answers: tuple, w_answers: tuple):
        """Inits the question"""
        self.sentence = sentence
        self.statement = statement
        self.c_answer = c_answers
        self.w_answer = w_answers
        self.answers = c_answers + w_answers
        shuffle(self.answers)

    def __repr__(self) -> str:
        return "\n\n".join([self.sentence, self.statement, "\n".join(self.answers)])
    
    def __str__(self) -> str:
        return "\n\n".join([self.sentence, self.statement, "\n".join(self.answers)])
    
    def get_choices(self) -> tuple:
        """Get user choices based on numerical index"""
        choices = []
        for i in range(len(self.c_answer)):
            user_input = int(input("Insert answer number\n")) - 1
            selected_answer = self.answers[user_input]
            choices.append(selected_answer)
        
        self.choices = choices

    def evaluate(self) -> bool:
        """Evaluate selected answers"""
        if set(self.choices) == set(self.c_answer):
            return True
        else:
            return False