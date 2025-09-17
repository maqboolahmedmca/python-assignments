# Project 6

Practice Test Conductor: Gives a practice test on a selected Chapter

## Requirements
* Provide a chapters selection input in the command line
* List questions & their options from the selected chapter
* Print one question at a time on the console 
* Ask the user to provide answer, validate it.

## Error Handling
    - Take care of case where empty string is provided as input from command line
    - Take care of case where there are no questions corresponding to the provided chapter name

Note: It uses Postgres Database

# Install dependencies
pip install psycopg2

# Content Resources
It uses local database to load the entities (Subject, Chapter, Question)

Note: Provide the database details in the dao/config.json

# How to Run?
python3 practice_test_conductor.py
