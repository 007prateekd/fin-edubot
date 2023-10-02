# fin-edubot

## What


## Why

## How
Download GGUF weights (comaptible with llama.cpp) from [link]. Clone this repo and run `conda env create -f environment.yml` to create a conda environment with all the dependencies. Activate the envronment using `conda activate edubot`. Web scraping code is provided in [scrape.py](scrape.py) and can be run simply by `python scrape.py`.


## To Do

- Make inference faster. Model compression?
- Create `streamlit` app?
- Provide ggml-to-gguf conversion script for custom llm model usage.