# fin-edubot

## What
A chatbot that uses llama-2 family of models and Retrieval-Augmented Generation (RAG) to answer your finance-related questions and cite its sources on your CPU. 

I have used [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) as the LLM as it has the fastest inference (of course after Karpathy's [llama2.c](https://github.com/karpathy/llama2.c)) on CPU. I scraped [Zerodha Varsity](https://zerodha.com/varsity/) and used this as the database for RAG. The LLM would refer to this database while answering your query and augment its generation process with this data. The ouptut provied by RAG is crisp and to the point to what the user asks compared to just the LLM's output while also citing the sources which helps the LLM provide conclusive argument and prevent hallucinations.

## Why

I wanted to try out the functionalities and capabilities of RAG using the popular [langchain](https://www.langchain.com/). What better to way to create your own chatbot using your own scraped data running inference on your own machine over the CPU? The "over the CPU" part is crucial since the smallest vanilla LLMs (like llama2-7B) were taking over an hour to generate outputs. This reduces to a minute when using llama-cpp-python.


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

## Results (and Comparison)
> Prompt: What are index funds? Describe in one line.

> LLM: Unterscheidung between active and passive management. Index funds are a type of mutual fund or exchange-traded fund (ETF) that tracks a particular market index, such as the S&P 500 or the Dow Jones Industrial Average, by holding a portfolio of securities that mirrors the performance of the index. In contrast to actively managed funds, which aim to outperform the market through research and analysis of individual securities, index funds do not attempt to beat the market but rather match its performance.

> RAG: Index funds are a type of mutual fund that passively tracks a market index, such as the S&P 500, by holding the same stocks in the same proportion as the index. 


## To Do

- Upload pretrained llama2.cpp GGUF weights.
- Make inference faster. Model compression?
- Create `streamlit` app.
- Provide GGML-to-GGUF conversion script for custom llm model usage.