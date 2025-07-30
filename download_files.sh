#!/bin/bash

OUTPUT_DIR=./out/
mkdir "$OUTPUT_DIR"

BOWLS=./data/bowls/
mkdir -p "$BOWLS"
curl https://www.csun.edu/science/ref/games/questions/97_phys.pdf > "$BOWLS"/phys.pdf
curl https://www.csun.edu/science/ref/games/questions/97_biol.pdf > "$BOWLS"/biol.pdf
curl https://www.csun.edu/science/ref/games/questions/97_chem.pdf > "$BOWLS"/chem.pdf

PROJECT_EULER=./data/project_euler/
mkdir -p "$PROJECT_EULER" "$PROJECT_EULER"/questions/ "$PROJECT_EULER"/answers/ "$PROJECT_EULER"/resources/images/
MAX_QUESTION_NUM=100
# Download the questions
for i in $(seq 1 "$MAX_QUESTION_NUM"); do
    curl https://projecteuler.net/minimal="$i" > "$PROJECT_EULER"/questions/"$i".txt
done
# Download the answers (verified robots.txt to allow scraping)
for i in $(seq 1 "$MAX_QUESTION_NUM"); do
    curl https://euler.stephan-brumme.com/"$i"/"$i".cpp > "$PROJECT_EULER"/answers/"$i".txt
done
