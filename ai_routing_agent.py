import os
from typing import List
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from word2number import w2n

from tools.text_summarizer import TextSummarizer
from tools.text_funifier import TextFunifier
from tools.multiplication_tool import MultiplicationTool
from tools.vowel_counter import VowelCounter

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Initialize tools
text_summarizer = TextSummarizer()
text_funifier = TextFunifier()
multiplication_tool = MultiplicationTool()
vowel_counter = VowelCounter()

# Initialize the language model
llm = OpenAI(temperature=0.5)

# Create the routing prompt
routing_prompt = PromptTemplate(
    input_variables=["input"],
    template="You are an AI assistant that routes user requests to the appropriate tool. "
             "Available tools are: Text Summarizer, Text Fun-ifier, Multiplication Tool, and Vowel Counter. "
             "Determine which tool to use based on the user's input.\n\n"
             "User Input: {input}\n"
             "Tool to use:"
)

# Create the routing chain
routing_chain = LLMChain(llm=llm, prompt=routing_prompt)

def preprocess_input(user_input: str) -> str:
    words = user_input.split()
    for i, word in enumerate(words):
        try:
            number = w2n.word_to_num(word)
            words[i] = str(number)
        except ValueError:
            pass
    return " ".join(words)

def route_tool(user_input: str) -> str:
    preprocessed_input = preprocess_input(user_input)
    response = routing_chain.run(preprocessed_input)
    return response.strip()

def run_tool(tool_name: str, user_input: str) -> str:
    preprocessed_input = preprocess_input(user_input)
    if "summarizer" in tool_name.lower():
        return text_summarizer.summarize(preprocessed_input)
    elif "fun-ifier" in tool_name.lower():
        return text_funifier.funify(preprocessed_input)
    elif "multiplication" in tool_name.lower():
        numbers = [int(s) for s in preprocessed_input.split() if s.isdigit()]
        return str(multiplication_tool.multiply(numbers))
    elif "vowel" in tool_name.lower():
        return str(vowel_counter.count(preprocessed_input))
    else:
        return "No appropriate tool found for this input."

def process_input(user_input: str) -> str:
    tool_name = route_tool(user_input)
    result = run_tool(tool_name, user_input)
    return f"{tool_name} Result: {result}"

if __name__ == "__main__":
    print("Welcome to the AI Routing Agent!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter your prompt: ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the AI Routing Agent. Goodbye!")
            break
        
        result = process_input(user_input)
        print(result)
