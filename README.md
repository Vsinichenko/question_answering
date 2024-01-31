# question_answering
Question Answering system using LLM and Langchain


### Description:
The objective of this task is to create a Question Answering (QA) system that looks up
through provided documents to retrieve or generate accurate, contextually relevant answers
to the given questions. Langchain is one option, since it lets us build such applications while
interacting with language models. You are free to integrate any open sourced LLMs, the
size of the LLMs depends on your hardware availability. Few suggestions here - LLAMA2,
MPT, Mistral (you can use colab here for inference). You're encouraged to establish a custom
pipeline for generating embeddings and handling QA functionality, even outside the use of
Langchain, as the emphasis will be on your problem-solving approach.

### Requirements:
**Vector Store and Embeddings**: You are free to you any models/techniques to generate/use
the embeddings (suggestions here - Chroma, Weaviate, FAISS)

**Factual Accuracy**: Ensure answers are extracted or inferred directly from the provided
document, maintaining factual consistency and not being completely made up
(Hallucinations)

**Code Quality**: Ensure that the code is structured, formatted, and documented according to
best practices.


 export OPENAI_API_KEY="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"