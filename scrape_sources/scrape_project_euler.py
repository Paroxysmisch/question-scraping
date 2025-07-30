import os
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class ProjectEulerQuestion:
    question: str
    images_paths: List[Path]
    answer_path: Path


def scrape(
    question_dir: Path, answer_dir: Path, image_dir: Path
) -> List[ProjectEulerQuestion]:
    NUM_QUESTIONS = sum(1 for f in question_dir.iterdir() if f.is_file())
    questions = []

    for i in range(1, 1 + NUM_QUESTIONS):
        question = None
        media = []
        answer = Path(f"{answer_dir}/{i}.txt")
        with open(f"{question_dir}/{i}.txt") as question_file:
            question = question_file.read()

            # Save all the images in the <img> tags
            soup = BeautifulSoup(question, "html.parser")
            output_dir = image_dir
            base_url = "https://projecteuler.net/"

            img_tags = soup.find_all("img")
            for img in img_tags:
                img_url = img.get("src")
                if not img_url:
                    continue

                # Handle relative URLs
                full_url = urljoin(base_url, img_url)

                try:
                    response = requests.get(full_url)
                    response.raise_for_status()

                    # Extract the image filename
                    filename = os.path.basename(full_url)
                    image_path = output_dir / filename

                    # Save the image
                    with open(image_path, "wb") as f:
                        f.write(response.content)

                    media.append(image_path)

                except requests.RequestException as e:
                    print(f"Failed to download {full_url}: {e}")

        project_euler_question = ProjectEulerQuestion(question, media, answer)
        questions.append(project_euler_question)

    return questions
