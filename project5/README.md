# Project 5
QuestionaireManager: It extracts question papar & stores the entities (Subject, Chapter, Question) in the postgres database.

## Requirements
* Update project 4 and add support for database
* Create a database to store the following
    - Subject
    - Chapter
    - Question
* Load a PDF containing questions
* Extract each question as per a regular expression
* Store each question in the database

## Error Handling
* Take care of case where database is not available
* Take care of case where table is not available
* Take care of any error handling in DB operations


Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf
pip install psycopg2

# Content Resources
It uses `/content/Chemistry Questions.pdf`, extracts the questionnaire & stores it in the local database.
Note: Provide the database details in the dao/config.json

# How to Run?
python3 questionnaire_manager.py
