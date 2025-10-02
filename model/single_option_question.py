from model.objective_question import ObjectiveQuestion

class SingleOptionQuestion(ObjectiveQuestion):

    def __init__(self, id: int, text: str, options: list[str], correct_answer: str, marks: int):
        super().__init__(id, 'single', text, options, correct_answer, marks)       
        print("SingleOptionQuestion : " + str(correct_answer))   