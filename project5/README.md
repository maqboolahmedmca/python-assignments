# What is it?

QuestionaireManager: It extracts question papar & stores the entities (Subject, Chapter, Question) in the postgres database.

Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf
pip install psycopg2

# Content Resources
It uses `/content/Chemistry Questions.pdf`, extracts the questionnaire & stores it in the local database.
Note: Provide the database details in the dao/config.json

# How to Run?
python3 questionnaire_manager.py
