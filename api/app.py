from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate # for ChatPromptTemplate
from langchain.chat_models import ChatOpenAI # for OpenAI
from langserve import add_routes # for adding routes
import uvicorn # for running the server
import os
from langchain_community.llms import Ollama # for using Ollama models
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="Langchain API Server",
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai",
# )
# model = ChatOpenAI()
# Ollama dolphin-llama3 LLM
llm = Ollama(model="dolphin-llama3")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

# add_routes(
#     app,
#     prompt1|model,
#     path="/essay"    
# )

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)