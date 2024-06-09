## Following Krish Naik on YT:

### With OpenAI Api key
1. First implemnting the chatbot with openai api key -> I don't have the key, so will not go in detail.

2. pip install -r requirements.txt, pip install -U langchain langchain-openai, following the setup from the langsmith project dashboard.

3. Writing the code for the chatbot, invoking the chain, streamlit run app.py

4. Chatbot just working fine, from langchain dashboard we can track everything -> input, outputparser, cost for that input, etc.

### With Open Source Ollama models
1. importing ollama from langchain_community.llms
2. Keeping the full code similar, just changing the model to ollama before involking the chain.