#!/bin/bash

BOWLS=./data/bowls/
mkdir -p "$BOWLS"
curl https://www.csun.edu/science/ref/games/questions/97_phys.pdf > "$BOWLS"/phys.pdf
curl https://www.csun.edu/science/ref/games/questions/97_biol.pdf > "$BOWLS"/biol.pdf
curl https://www.csun.edu/science/ref/games/questions/97_chem.pdf > "$BOWLS"/chem.pdf
