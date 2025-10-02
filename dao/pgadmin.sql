
CREATE TABLE public.subject (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE public.chapter (
    id SERIAL PRIMARY KEY,
    subject_id INT NOT NULL REFERENCES subject(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE public.question (
    id SERIAL PRIMARY KEY,
    chapter_id INT NOT NULL REFERENCES chapter(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
	option_a VARCHAR(255),
	option_b VARCHAR(255),
	option_c VARCHAR(255),
	option_d VARCHAR(255),
    answer_option VARCHAR(255) NOT NULL
);

ALTER TABLE chapter
ADD CONSTRAINT unique_subject_chapter UNIQUE (subject_id, name);

ALTER TABLE question
ADD CONSTRAINT unique_chapter_question UNIQUE (chapter_id, question_text);

select * from subject;
select * from chapter;
select * from question;

-- delete from subject;
-- delete from chapter;
-- delete from question;

-- project8: table-per-subclass approach
-- Base table (all questions)
CREATE TABLE base_question (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,   -- "single", "multi", "match", "truefalse", "descriptive"
    text TEXT NOT NULL,
    marks INT NOT NULL
);

-- Objective questions (Single | Multi | Match | TrueFalse)
CREATE TABLE objective_question (
    id INT PRIMARY KEY REFERENCES base_question(id) ON DELETE CASCADE,
    options JSONB NOT NULL,
    correct_answer JSONB NOT NULL
);

-- Descriptive questions
CREATE TABLE descriptive_questions (
    id INT PRIMARY KEY REFERENCES base_question(id) ON DELETE CASCADE,
    keywords JSONB
);


select b.* from base_question b
select o.* from objective_question o

select b.*, o.options, o.correct_answer from base_question b
	left join objective_question o on b.id = o.id

delete from base_question b where b.id = 5

TRUNCATE objective_question, descriptive_questions, base_question RESTART IDENTITY CASCADE;
