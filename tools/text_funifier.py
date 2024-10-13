from langchain_core.tools import tool
from langchain_groq import ChatGroq
import os


API_KEY = os.environ.get("API_TOKEN", "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")


llm = None
@tool
def initialize_llm(api_key: str):
    """Initialize the LLM with the provided API key.

    Args:
        api_key (str): The API key for accessing the language model.
    """
    global llm
    llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", api_key=api_key)
    return "LLM initialized successfully."
initialize_llm(API_KEY)
@tool
def llm_text_funifier(text: str) -> str:
    """Make the given text funnier while retaining its original meaning."""
    prompt = f"Make the following text funnier while retaining its original meaning(add humor to the textEnsure the output is coherent and contextually appropriat):\n\n{text}"
    response = llm.invoke(prompt)
    return response.content