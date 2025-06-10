from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(query):
    prompt = ChatPromptTemplate.from_template("Answer this: {question}")
    chain = prompt | llm
    return chain.invoke({"question": query})
