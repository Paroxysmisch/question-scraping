from dataclasses import dataclass
from pathlib import Path
from typing import List, Literal

from scrape_sources import scrape_bowl, scrape_project_euler


@dataclass
class Problem:
    question_type: Literal["Multiple Choice", "Short Answer", "Code"]
    question: str
    answer: str | None = None
    choices: List[str] | None = None
    images_paths: List[str] | None = None
    answer_path: str | None = None


def merge_into_problem(
    problem: scrape_bowl.BowlQuestion | scrape_project_euler.ProjectEulerQuestion,
) -> Problem:
    if isinstance(problem, scrape_bowl.BowlQuestion):
        return Problem(
            question_type=problem.question_type,
            question=problem.question,
            answer=problem.answer,
            choices=(
                problem.choices if problem.question_type == "Multiple Choice" else None
            ),
        )
    else:
        return Problem(
            question_type="Code",
            question=problem.question,
            answer=None,
            images_paths=[
                str(path) for path in problem.images_paths
            ],  # Convert from Path objects to just str
            answer_path=str(problem.answer_path),
        )


def main():
    problems = []

    problems.extend(scrape_bowl.scrape(Path("./data/bowls/phys.pdf"), "PHYS-"))
    problems.extend(scrape_bowl.scrape(Path("./data/bowls/biol.pdf"), "BIOL-"))
    problems.extend(scrape_bowl.scrape(Path("./data/bowls/chem.pdf"), "CHEM-"))

    question_dir = Path("./data/project_euler/questions/")
    answer_dir = Path("./data/project_euler/answers/")
    image_dir = Path("./data/project_euler/resources/images/")
    problems.extend(scrape_project_euler.scrape(question_dir, answer_dir, image_dir))

    problems = list(map(lambda x: merge_into_problem(x), problems))

    breakpoint()


if __name__ == "__main__":
    main()
