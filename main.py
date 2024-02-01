import pwinput
import os
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# noinspection PyUnresolvedReferences
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate

from config import example_directory


class QuestionAnsweringSystem:

    def __enter__(self):
        os.environ["OPENAI_API_KEY"] = pwinput.pwinput(
            "Enter OpenAI API key, " "see https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key \n"
        )
        print()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def main(self):
        loader = DirectoryLoader(f"examples/{example_directory}/sources")

        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
        retriever = vectorstore.as_retriever()

        prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="You are an assistant for question-answering tasks. Use the following pieces of retrieved context "
            "to answer the question. If you don't know the answer, just say that you don't know. "
            "Use three sentences maximum and keep the answer concise. Do not add the general facts known to you "
            "to augment the answer, just focus on the information provided. "
            "\nQuestion: {question} \nContext: {context} \nAnswer:",
        )

        human_message_prompt_template = HumanMessagePromptTemplate(prompt=prompt_template)

        custom_prompt = ChatPromptTemplate(
            input_variables=["context", "question"],
            messages=[human_message_prompt_template],
        )

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | custom_prompt
            | llm
            | StrOutputParser()
        )

        # print(
        #     rag_chain.invoke(
        #         "Which teams played in the NFL Kickoff Game to begin the 2022 season, and what was the result?"
        #     )
        # )

        questions = ["Hello, how are you doing?"]
        questions_data = open(f"examples/{example_directory}/questions.txt").read()
        questions_provided = questions_data.split("\n")
        questions.extend(questions_provided)

        for q in questions:
            print(f"QUESTION: {q}")
            print("ANSWER: " + rag_chain.invoke(q))
            print()


if __name__ == "__main__":
    with QuestionAnsweringSystem() as qa_system:
        qa_system.main()
