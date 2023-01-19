import json
from random import choice

class Parser:
    """Question Parser class

    Attributes:
        questions: list with loaded Questions
        c_answer: A tuple wich contains the correct answers
        w_answer: A tuple wich contains the incorrect answers
    """
    def __init__(self, file_route):
        with open(file_route) as file_route:
            self.questions = json.load(file_route)['Questions']
    
    def random_question(self):
        return choice(self.questions)
