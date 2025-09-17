
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
