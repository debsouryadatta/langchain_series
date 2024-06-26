from langchain_core.prompts import ChatPromptTemplate # for ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # for StrOutputParser
from langchain_community.llms import Ollama # for using Ollama models


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



# Promot Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# Streamlit Framework
st.title('Langchain Demo With Llama3 API')
input_text=st.text_input("Search the topic u want")

# Ollama dolphin-llama3 LLM
llm = Ollama(model="dolphin-llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))