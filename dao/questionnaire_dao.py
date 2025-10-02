from dao.db_util import init_db_pool, get_connection, release_connection
from dao.config_loader import ConfigLoader
from model.question import Question
from model.subject import Subject
from model.chapter import Chapter   
from model.base_question import BaseQuestion
from model.objective_question import ObjectiveQuestion
from model.single_option_question import SingleOptionQuestion
from model.multiple_options_question import MultipleOptionsQuestion
from typing import List
from psycopg2.extras import Json

class QuestionnaireDao:
    def __init__(self):
        self.db_config = ConfigLoader().get_config()
        self.db_pool = init_db_pool(db_config=self.db_config)
    
    def store_subject(self, subject: Subject):
        """
        Stores a Subject in the database.
        If the subject already exists (by name), updates it.
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check if subject exists
            cursor.execute("SELECT id FROM subject WHERE name = %s", (subject.name,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute("UPDATE subject SET name = %s WHERE id = %s", (subject.name, existing[0],))
                subject.id = existing[0]
                print(f"Updated subject: {subject.name} (ID: {subject.id})")
            else:
                cursor.execute(
                    "INSERT INTO subject (name) VALUES (%s) RETURNING id",
                    (subject.name,)
                )
                subject.id = cursor.fetchone()[0]
                print(f"Inserted subject: {subject.name} (ID: {subject.id})")

            conn.commit()
            return subject

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error storing subject: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)
    
    def store_chapter(self, chapter: Chapter):
        """
        Stores a Chapter in the database, linked to a subject.
        If the chapter already exists (name and subject_id), updates it.
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check if chapter exists for this subject
            cursor.execute(
                "SELECT id FROM chapter WHERE name = %s AND subject_id = %s",
                (chapter.name, chapter.subject_id,)
            )
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    "UPDATE chapter SET name = %s WHERE id = %s",
                    (chapter.name, existing[0],)
                )
                chapter.id = existing[0]
                print(f"Updated chapter: {chapter.name} (ID: {chapter.id})")
            else:
                cursor.execute(
                    "INSERT INTO chapter (name, subject_id) VALUES (%s, %s) RETURNING id",
                    (chapter.name, chapter.subject_id,)
                )
                chapter.id = cursor.fetchone()[0]
                print(f"Inserted chapter: {chapter.name} (ID: {chapter.id})")

            conn.commit()
            return chapter

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error storing chapter: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)

    def store_question(self, question: Question):
        """
        Stores a Question in the database, linked to a chapter.
        If the question already exists (by text and chapter_id), updates it.
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check if question exists for this chapter
            cursor.execute(
                "SELECT id FROM question WHERE question_text = %s AND chapter_id = %s",
                (question.text, question.chapter_id)
            )
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    """
                    UPDATE question
                    SET chapter_id = %s, question_text = %s, option_a = %s, option_b = %s, option_c = %s, option_d = %s, answer_option = %s
                    WHERE id = %s
                    """,
                    (
                        question.chapter_id,
                        question.text,
                        question.option_a,
                        question.option_b,
                        question.option_c,
                        question.option_d,
                        question.answer,
                        existing[0],
                    )
                )
                question.id = existing[0]
                print(f"Updated question ID: {question.id} for chapter ID: {question.chapter_id}")
            else:
                cursor.execute(
                    """
                    INSERT INTO question
                    (question_text, option_a, option_b, option_c, option_d, answer_option, chapter_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        question.text,
                        question.option_a,
                        question.option_b,
                        question.option_c,
                        question.option_d,
                        question.answer,
                        question.chapter_id,
                    )
                )
                question.id = cursor.fetchone()[0]
                print(f"Inserted question ID: {question.id} for chapter ID: {question.chapter_id}")

            conn.commit()
            return question

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error storing question: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)

    
    def list_chapters(self) -> List["Chapter"]:
        """
        List Chapters from the database
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, subject_id, name  FROM chapter"
            )
            return [Chapter(id=row[0], subject_id=row[1], name=row[2]) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error listing chapter: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)
    
    def get_questions_by_chapter(self, chapter_id: int) -> List["Question"]:
        """
        Get Questions by chapter_id from the database
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, chapter_id, question_text, option_a, option_b, option_c, option_d, answer_option FROM question WHERE chapter_id = %s",
                (chapter_id,)
            )
            return [Question(id=row[0], chapter_id=row[1], text=row[2], option_a=row[3], option_b=row[4], option_c=row[5], option_d=row[6], answer=row[7]) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error getting questions by chapter: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)
    
    def insert_type_question(self, question: BaseQuestion) -> int:
        """
        Insert question into base_question and subclass tables.
        Returns the generated question id.
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            # 1. Insert into base_question
            cur.execute(
                """
                INSERT INTO base_question (type, text, marks)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (question.type, question.text, question.marks),
            )
            qid = cur.fetchone()[0]

            # 2. Insert into subclass table
            if isinstance(question, ObjectiveQuestion):
                # objective question (single or multiple)
                cur.execute(
                    """
                    INSERT INTO objective_question (id, options, correct_answer)
                    VALUES (%s, %s, %s)
                    """,
                    (qid, Json(question.options), Json(question.correct_answer)),
                )
            else:  # descriptive
                cur.execute(
                    """
                    INSERT INTO descriptive_questions (id, keywords)
                    VALUES (%s, %s)
                    """,
                    (qid, Json(question.correct_answer)),
                )

            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error storing type question: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)
        return qid
    
    def get_type_question_by_text(self, question_text):
        """
        Gets question by it's text.
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT id, type, text, marks FROM base_question WHERE text = %s",
                (question_text,)
            )
            row = cur.fetchone()
            if not row:
                return None
            return self.map_row_to_type_question(row, cur)
        except Exception as e:
            print(f"Error getting type question: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)
    
    def list_type_questions(self):
        """
        List type questions.
        """
        conn = None
        cursor = None
        type_questions = []
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT id, type, text, marks FROM base_question"
            )
            rows = cur.fetchall()
            for row in rows:
                type_question = self.map_row_to_type_question(row, cur)
                type_questions.append(type_question)

            return type_questions
        except Exception as e:
            print(f"Error list type questions: {e}")
            raise e

        finally:
            if cursor:
                cursor.close()
            if conn:
                release_connection(conn)

    def map_row_to_type_question(self, row, cur):
        qid, qtype, text, marks = row
        if qtype in ('single', 'multiple'):
            cur.execute(
                "SELECT options, correct_answer FROM objective_question WHERE id = %s",
                (qid,)
            )
            obj_row = cur.fetchone()
            if not obj_row:
                return None
            options, correct_answer = obj_row

            if (qtype == 'single'):
                return SingleOptionQuestion(id=qid, text=text, options=options, correct_answer=correct_answer, marks=marks)
            elif (qtype == 'multiple'):
                return MultipleOptionsQuestion(id=qid, text=text, options=options, correct_answer=correct_answer, marks=marks)
            else:
                return None
        elif qtype == 'descriptive':
            cur.execute(
                "SELECT keywords FROM descriptive_questions WHERE id = %s",
                (qid,)
            )
            desc_row = cur.fetchone()
            if not desc_row:
                return None
            keywords = desc_row[0]
            return BaseQuestion(id=qid, text=text, marks=marks, correct_answer=keywords)
        else:
            print(f"Unknown question type: {qtype}")
            return None



