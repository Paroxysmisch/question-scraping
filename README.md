# question-scraping
## What does this project do?
Questions, along with their answers, and any additional resources, such as images, are scraped from two main sources.

These are then put into a final JSON format, where each entry represents a problem (question, answer, images, etc.).

## Sources
The two main sources are:
- Physics, Biology, and Chemistry Bowls from [csun.edu](https://www.csun.edu/). There is a PDF file containing questions and answers for each Bowl, which is parsed.
- [Project Euler](https://projecteuler.net/) provides questions (and associated diagrams), with the answers provided by https://euler.stephan-brumme.com/.

All sources were checked to see if scraping them was allowed (including checking the `robots.txt` file).

## Code architecture overview
The idea behind this code base is to make question scraping modular for each type of source. The `scrape_sources` directory provides two Python modules for scraping the two main sources (Bowls and Project Euler). Note that the Bowls scraping module, `scrape_bowl.py`, is designed to be general enough to scrape Physics, Biology, and Chemistry Bowls using the same code.

Each of the scraping modules outputs a `List` of its own problem type (they are Python dataclasses). These are `BowlQuestion` and `ProjectEulerQuestion`.

`main.py` is responsible for aggregating the different problem types into a unified format (called `Problem`), which is then output as JSON (along with its corresponding JSON schema) in the `./out/` directory.

This project makes use of Python type-checking (and also Pydantic) and the UV package manager to pin dependencies.

## Use
1. Clone the repository
2. From the repository root, run `uv sync`
3. Source the virtual environment with `. .venv/bin/activate` (bash), or `. .venv/bin/activate.fish` (fish)
4. Download the data with `./download_files.sh`
5. Run the scraping with `uv run main.py`
