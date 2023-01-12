class Question:
    """Basic Question class

    Attributes:
        qtype: A String which indicates the question type
        c_answer: A tuple wich contains the correct answers
        w_answer: A tuple wich contains the incorrect answers
    """

    def __init__(self, qtype, subject, c_answer: tuple, w_answer: tuple):
        """Inits the question"""
        self.qtype = qtype
        self.subject = subject
        self.c_answer = c_answer
        self.w_answer = w_answer

    def evaluate(self):
        """Evaluate selected answers"""
        passed = None

        
        return True
