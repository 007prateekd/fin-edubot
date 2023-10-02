# fin-edubot

## What
A chatbot that uses llama-2 family of models and Retrieval-Augmented Generation (RAG) to answer your finance-related questions on your CPU. 

I have used [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) as the LLM as it has the fastest inference on CPU. I scraped [Zerodha Varsity](https://zerodha.com/varsity/) and used this as the database for RAG. The LLM would refer to this database while answering your query and augment its generation process with this data. The ouptut provied by RAG is crisp and to the point to what the user asks compared to just the LLM's output (comparison provided in [notebook](rag.ipynb)).

## Why

I wanted to try out the functionalities and capabilities of [langchain](https://www.langchain.com/). What better to way to create your own chatbot using your own scraped data running inference on your own machine over the CPU?

"over the CPU" is the most crucial part since the smallest vanilla LLMs (like llama2-7B) were taking over an hour to generate outputs. This reduces to a minute when using llama-cpp-python.


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