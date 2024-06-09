## LangChain Series by Krish Naik on YT:

### Building Chatbot Using Paid And Open Source LLM's using Langchain And Ollama
1. First implemnting the chatbot with openai api key -> I don't have the key, so will not go in detail.

2. pip install -r requirements.txt, pip install -U langchain langchain-openai, following the setup from the langsmith project dashboard.

3. Writing the code for the chatbot, invoking the chain, streamlit run app.py

4. Chatbot just working fine, from langchain dashboard we can track everything -> input, outputparser, cost for that input, etc.

5. Now implemnting the chatbot with Open Source Ollama models, importing ollama from langchain_community.llms

6. Keeping the full code similar, just changing the model to ollama before involking the chain.


### Production Grade Deployment LLM As API With Langchain And FastAPI
7. pip install -r requirements.txt, new requirements.txt -> langserve, fastapi, uvicorn, sse_starlette
8. Creating the FastApi app, adding routes to it
9. Writing the prompt and the model, adding them to the routes
10. Running the app with uvicorn, python app.py -> server started on port 8000
11. Creating the streamlit app in client.py, writing get_openai_response func -> calling to "/essay/invoke" route, writing the get_ollama_response func -> calling to "/poem/invoke" route
12. Running the streamlit app -> streamlit run client.py
13. Since I dont have the OpenAI API key, so I just tested out for the Ollama model, and it worked fine. 