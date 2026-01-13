from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)




retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.7}
)


from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """You are an information extraction assistant.

Task:
- Identify the single entity from the question.
- Find relevant text about it in context.
- Rephrase the key fact naturally in your own words.
- Output ONLY one clear, concise sentence starting with "The [entity] [fact]."

Rules:
- Always rephrase—never copy text verbatim.
- Ignore unrelated content, lists, or extras.
- If no exact info, output: "I don't know."

Context:
{context}

Question:
{question}

Answer:"""
)





from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
hf_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=64,
    temperature=0,
    do_sample=False
)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

import re

def clean_output(text):
    # Strip extras, ensure single sentence
    text = re.sub(r'^\d+\.?\s*', '', text.strip())  # Remove numbering
    text = re.sub(r'\n.*', '', text)  # Single line
    if not text or text == "I don't know.":
        return text
    return text[0].upper() + text[1:] + "."


from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain=({"context": retriever | format_docs, "question": RunnablePassthrough()}
           | prompt
           | llm
           | StrOutputParser()
           | clean_output)

def get_answer(question: str) -> str:
    return rag_chain.invoke(question)
