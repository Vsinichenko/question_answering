# Question Answering System
This is a Question Answering system using LLM and Langchain.

The application answers questions based on the provided text.

### How to use the Tool
First, go to https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key and obtain the OpenAI API key.
It should start with "sk-"

In terminal, run:
`export OPENAI_API_KEY="your openai key here"`

Then, run `python main.py`

To use your custom example, create a folder inside `examples` and organize is similar to the `NFLseason` sample. You may provide multiple sources. Different languages are supported.

Then, go to `config.py` and modify the folder name. 

### How factualy accuracy is maintained
To maintain factual accuracy, I set `temperature` parameter of the ChatOpenAI LLM to 0. This parameter stands for model "creativity".

I noticed that the model, with the standard prompt for QA `hub.pull("rlm/rag-prompt")`, does not hallucinate on the provided sample questions. 
However, when I asked a question
```
QUESTION: What is NFL?
 ```
 the answer was:
```
ANSWER: The NFL stands for the National Football League. 
It is a professional American football league that consists of 32 teams. 
The league organizes the annual NFL season, which includes regular-season 
games, playoffs, and the Super Bowl.
```

The information about 32 teams was not given in the data source, although it is correct.

To make the QA system stick even more to the provided data source, I augmented the standard prompt with the sentence:
```
Do not add the general facts known to you to augment the answer, just focus on the information provided.
```
Now, the answer is:
``` 
ANSWER: The NFL stands for the National Football League.
```

### Task Description:
The objective of this task is to create a Question Answering (QA) system that looks up
through provided documents to retrieve or generate accurate, contextually relevant answers
to the given questions. Langchain is one option, since it lets us build such applications while
interacting with language models. You are free to integrate any open sourced LLMs, the
size of the LLMs depends on your hardware availability. Few suggestions here - LLAMA2,
MPT, Mistral (you can use colab here for inference). You're encouraged to establish a custom
pipeline for generating embeddings and handling QA functionality, even outside the use of
Langchain, as the emphasis will be on your problem-solving approach.

### Task Requirements:
**Vector Store and Embeddings**: You are free to you any models/techniques to generate/use
the embeddings (suggestions here - Chroma, Weaviate, FAISS)

**Factual Accuracy**: Ensure answers are extracted or inferred directly from the provided
document, maintaining factual consistency and not being completely made up
(Hallucinations)

**Code Quality**: Ensure that the code is structured, formatted, and documented according to
best practices.
