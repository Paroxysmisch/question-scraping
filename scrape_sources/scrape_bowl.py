from dataclasses import dataclass
from pathlib import Path
from typing import List, Literal, Tuple

import pdfplumber


@dataclass
class BowlQuestion:
    question_type: Literal["Multiple Choice", "Short Answer"]
    question: str
    choices: List[str] | None
    answer: str


def extract_questions(
    lines_txt: List[str], line_number: int, question_prefix: str
) -> Tuple[BowlQuestion | None, int | None]:
    # Find the start of the next question
    while line_number < len(lines_txt):
        if lines_txt[line_number].startswith(question_prefix):
            break
        line_number += 1

    # Early exit if no more questions
    if line_number >= len(lines_txt):
        return None, line_number

    # Read the question type
    question_type = None
    if "Multiple Choice" in lines_txt[line_number]:
        question_type = "Multiple Choice"
    else:
        question_type = "Short Answer"

    # Read the question
    question = lines_txt[line_number].split(": ")[1]
    line_number += 1
    while line_number < len(lines_txt) and not lines_txt[line_number].startswith(
        ("w)", "ANSWER")
    ):
        question += " "
        question += lines_txt[line_number]
        line_number += 1

    # Read the choices (if Multiple Choice)
    choices = None
    if question_type == "Multiple Choice":
        choices = []
        while line_number < len(lines_txt) and not lines_txt[line_number].startswith(
            "ANSWER"
        ):
            choice_split = lines_txt[line_number].split(") ")
            if len(choice_split) > 1:
                choices.append(choice_split[1])
            else:
                # The choice spans multiple lines
                choices[-1] += choice_split[0]
            line_number += 1

    # Read the answer
    while line_number < len(lines_txt) and not lines_txt[line_number].startswith(
        "ANSWER"
    ):
        line_number += 1

    answer = ""
    while line_number < len(lines_txt) and not lines_txt[line_number].startswith(
        (question_prefix, "Phys", "Biol", "Chem")
    ):
        answer += lines_txt[line_number]
        line_number += 1

    answer = answer.split("ANSWER: ")[1]  # Remove "ANSWER: "

    return BowlQuestion(question_type, question, choices, answer), line_number


def scrape(file_path: Path, question_prefix: str) -> List[BowlQuestion]:
    pdf = pdfplumber.open(file_path)

    for page in pdf.pages:
        lines = page.extract_text_lines()
        lines_txt = []

        # Extract text from data dictionary
        for line in lines:
            lines_txt.append(line["text"])

        line_number = 0
        while line_number < len(lines_txt):
            bowl_questions, new_line_number = extract_questions(
                lines_txt, line_number, question_prefix
            )
            print(bowl_questions)
            line_number = new_line_number

    return []
