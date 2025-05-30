import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_objectbox.vectorstores import ObjectBox
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv

load_dotenv()

# load the Groq api key

groq_key=os.environ['GROQ_API_KEY']


st.title("Objectbox VectorStoreDB with Llama3 Demo")

llm=ChatGroq(groq_api_key=groq_key,model_name="llama-3.1-8b-instant")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the context only.
Please provide the most accurate response based on the question
{context}
Question:{input}

"""
)

## Vector Embedding and Object Vectorstore db


def vector_emebdding():

    if "vectors" not in st.session_state:
        st.session_state.embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.loader=PyPDFDirectoryLoader("./us_census") ##Data Ingestion
        st.session_state.doc=st.session_state.loader.load() #Documents Laoding
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.doc)
        st.session_state.vectors=ObjectBox.from_documents(st.session_state.final_documents,st.session_state.embeddings,embedding_dimensions=768)



input_prompt=st.text_input("Enter Your Question From Documents")

if st.button("Documents Embedding"):
    vector_emebdding()
    st.write("ObjectBox DataBase is ready")


import time

if input_prompt:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()


    response=retrieval_chain.invoke({'input':input_prompt}) 
    
    print("Response Time:",time.process_time()-start)
    st.write(response['answer'])

    #with streamlit expander
    with st.expander("Document Similarity Search"):
     #Find The Relevant Chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("------------------------------------")




