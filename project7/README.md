# Project 7

RSS Feed Extractor: Load RSS content and then extract content from each link. Do this in multiple threads
Requirements

Error Handling
Take care of case where no RSS xml file is available
Take care of case where xml file is empty


## Requirements
* Load an RSS xml file (Format: https://www.w3schools.com/xml/xml_rss.asp)
* Loop through each link
* Extract content from each link and write to “output.txt”
* Execute reading from multiple links in parallel

## Error Handling
    - Take care of case where no RSS xml file is available
    - Take care of case where xml file is empty


Note: It uses Postgres Database

# Install dependencies
pip install feedparser

# Content Resources
It uses local database to load the entities (Subject, Chapter, Question)

Note: Provide the database details in the dao/config.json

# How to Run?
python3 practice_test_conductor.py
