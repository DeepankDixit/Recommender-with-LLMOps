from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender: 
    #idea: I need 3 things for making recommendations: prompt, retriever, and LLM (which requires API key and model name)
    def __init__(self, retriever, api_key:str, model_name:str):
        self.llm = ChatGroq(
            api_key = api_key,
            model = model_name,
            temperature=0
        )
        self.prompt = get_anime_prompt()
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type="stuff", # "stuff" means it will use the full document content
            retriver = retriever,
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": self.prompt
            }
        )
    
    def get_recommendation(self, query:str):
        response = self.qa_chain.invoke({"query": query})
        return response['result'], response['source_documents']
        #result is the answer to the query, source_documents are the documents used to generate the answer
        #Note: source_documents is a list of Document objects, each containing metadata and page content
        #You can access the metadata and page content using response['source_documents'][0].metadata