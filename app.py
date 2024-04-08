from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assistant. Please response to the user request only based on the given context. Do not provide any information that is not in the context"),
        ("user", "Question:{question}\nContext:{context}"),
        
    ]
)
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|model|output_parser
question = "Can you summarize the speech?"
# write a speech
context = """
The speech was about the importance of education in the modern world.
The speaker emphasized that education is the key to success and that it is important to invest in education.
The speaker also mentioned that education is a fundamental human right and that everyone should have access to
quality education. The speech concluded by stating that education is the foundation of a prosperous society
and that it is essential for the development of individuals and communities.
"""
print(chain.invoke({"question": question, "context": context}))