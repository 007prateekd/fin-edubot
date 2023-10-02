# fin-edubot

## What


## Why

## How
Download GGUF weights (comaptible with llama.cpp) from [link]. Run the following commands to create and activate the necessary conda environment: 
```
conda env create -f environment.yml
conda activate edubot
```
Web scraping code is provided in [scrape.py](scrape.py) and can be run simply by `python scrape.py`.


## To Do

- Make inference faster. Model compression?
- Create `streamlit` app.
- Provide GGML-to-GGUF conversion script for custom llm model usage.