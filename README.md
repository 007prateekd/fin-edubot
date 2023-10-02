# fin-edubot

## What
A chatbot that uses LLAMA-2 family of models and Retrieval-Augmented Generation (RAG) to answer your finance-related questions on your CPU. 

I have used [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) as the LLM as it has the fastest inference on CPU. I scraped [Zerodha Varisty](https://zerodha.com/varsity/) and used this as the database for RAG. The LLM would refer to this database while answering your query and augment its generation process with this data. 

## Why

## How
Download GGUF weights (comaptible with llama.cpp) from [link]. Run the following commands to create and activate the necessary conda environment: 
```
conda env create -f environment.yml
conda activate edubot
```
Web scraping code is provided in [scrape.py](scrape.py) and can be run simply by:
```
python scrape.py
```
Finally, the actual chatbot code is in [rag.ipynb](rag.ipynb).

## To Do

- Upload pretrained llama2.cpp GGUF weights.
- Make inference faster. Model compression?
- Create `streamlit` app.
- Provide GGML-to-GGUF conversion script for custom llm model usage.