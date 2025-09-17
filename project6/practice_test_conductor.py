from dao.questionnaire_dao import QuestionnaireDao

class PracticeTestConductor:
    def __init__(self):
        self.dao = QuestionnaireDao()

    def start_test(self):
        try:
            chapters = self.dao.list_chapters()
            if not chapters:
                print("No chapters available for the practice test.")
                return
            print("Available Chapters:")
            for idx, chapter in enumerate(chapters, start=1):
                print(f"{idx}. {chapter.name}")
            
            choice = int(input("Select a chapter by number: ")) - 1
            while choice < 0 or choice >= len(chapters):
                choice = int(input("Invalid choice. Please select a valid chapter number: ")) - 1
            selected_chapter = chapters[choice]
            questions = self.dao.get_questions_by_chapter(selected_chapter.id)

            if not questions:
                print("No questions available for the selected chapter: {selected_chapter.name}")
                return
            score = 0
            for question in questions:
                print(f"\nQ: {question.text}")
                print(f"A) {question.option_a}")
                print(f"B) {question.option_b}")
                print(f"C) {question.option_c}")
                print(f"D) {question.option_d}")
                answer = input("Your answer (A/B/C/D): ").strip().upper()

                while answer not in ['A', 'B', 'C', 'D']:
                    answer = input("Invalid choice. Please enter A, B, C, or D: ").strip().upper()

                if answer == question.answer:
                    score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is {question.answer}.")
                
                choice = input("Press Enter to continue or type 'q' to quit: ")
                if choice.strip().lower() == "q":
                    break
            
            print(f"\nYour total score: {score}/{len(questions)}")
        except Exception as e:
            print(f"An error occurred: {e}")

testConductor = PracticeTestConductor()
choice=input('Are you ready to start the practice test? (y/n): ')
if choice.lower() == 'y':
    print("Starting the practice test...")
    testConductor.start_test()
else:
    print("Practice test aborted.")



