from model.objective_question import ObjectiveQuestion

class MultipleOptionsQuestion(ObjectiveQuestion):

    def __init__(self, id: int, text: str, options: list[str], correct_answer: str, marks: int):
        super().__init__(id, 'multiple', text, options, correct_answer, marks)        
        print("MultipleOptionsQuestion : " + str(correct_answer))