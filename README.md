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

### Getting Started With RAG Pipeline Using Langchain Chromadb And FAISS
14. RAG(Retrieval Augmented Generation) Pipeline flow -> Load, Break into chunks, Embed, Vector Store, Query, Generate

15. pip install ipykernel, writing the code for loading the text from speech.txt file

16. Loading the openai api key from the .env

17. pip install -r requirements.txt, new requirements.txt -> bs4, pypdf, chromadb, faiss-cpu

18. Writing the code for loading the text_documents from Web Page, also using bs4 library for this

19. Writing the code for loading the text_documents from PDF, also using pypdf library for this

20. Loading the text_documents part is done

21. Now, Dividing the documents into chunks of 1000 words, writing the code for this

22. Now converting the chunks into vector embeddings, and storing it into vector database

23. Using Chroma db for vector database, OpenAIEmbeddings for vector embeddings(Need openai api key for this, so couldn't implement this) -> Try to use OllamaEmbeddings for the same

24. Querying the vector store, and retrieving the similar documents

25. Using FAISS for the vector store, writing the code for this