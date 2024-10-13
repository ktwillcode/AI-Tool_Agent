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
def llm_text_summarizer(text: str) -> str:
    """Summarize the given text using an LLM.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summarized text.

    Raises:
        ValueError: If the LLM is not initialized.
    """
    if llm is None:
        raise ValueError("LLM not initialized. Please call initialize_llm first.")
    
    prompt = f"Summarize the following text concisely:\n\n{text}"
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        raise RuntimeError(f"Error invoking LLM: {e}")
