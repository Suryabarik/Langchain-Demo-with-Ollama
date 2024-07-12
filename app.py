from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama

# Load environment variables from .env file
load_dotenv()

# Ensure LANGCHAIN_API_KEY is set
api_key = os.getenv("LANGCHAIN_API_KEY")
if api_key is None:
    raise ValueError("The LANGCHAIN_API_KEY environment variable is not set.")

# Set environment variables
os.environ['LANGCHAIN_API_KEY'] = api_key

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Define the model
llm = Ollama(model="gemma")

# Define the prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# Add routes
add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
