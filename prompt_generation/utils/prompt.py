import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.vectorstores import Pinecone

class ChatWithPinecone:
    def __init__(self, openai_api_key, pinecone_api_key, pinecone_index, model='gpt-3.5-turbo', text_field='text'):
        load_dotenv()
        self.openai_key = os.getenv(openai_api_key)
        self.pinecone_key = os.getenv(pinecone_api_key)
        self.pinecone_index = os.getenv(pinecone_index)
        self.model = model
        self.text_field = text_field
        self.chat = ChatOpenAI(openai_api_key=self.openai_key, model=self.model)
        self.vectorstore = Pinecone(index=self.pinecone_index, embed_query=self.embed_query, text_field=self.text_field)

    def embed_query(self, query):
        return self.chat([HumanMessage(content=query)])[0].metadata['embedding']

    def chat_and_search(self, user_messages, query, k=3):
        response = self.chat(user_messages)
        embedding = response[-1].metadata['embedding']
        vectorstore.similarity_search(embedding, k=k)

if __name__ == "__main__":
    openai_api_key = "OPENAI_API_KEY"
    pinecone_api_key = "PINECONE_API_KEY"
    pinecone_index = "PINECONE_INDEX"

    user_messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hi AI, how are you today?"),
        AIMessage(content="I'm great thank you. How can I help you?"),
        HumanMessage(content="I'd like to understand string theory.")
    ]

    chat_handler = ChatWithPinecone(openai_api_key, pinecone_api_key, pinecone_index)
    chat_handler.chat_and_search(user_messages, query="What is this challenge week about?", k=3)
