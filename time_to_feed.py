from src.question import  Question
from src.db import Parser
# from src.db import

file_route = "src/Assets/questions.json"

# Load questions
parser = Parser(file_route=file_route)

# Random Question
question = parser.random_question()
question = Question(**question)

# Show question and get choices
print(question)
question.get_choices()

# Eval question:
options = question.evaluate()
print(options)