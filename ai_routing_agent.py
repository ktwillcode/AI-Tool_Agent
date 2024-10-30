import os

from datetime import datetime
from typing import Annotated, TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from langchain_groq import ChatGroq

from tools import llm_text_summarizer, llm_text_funifier, multiplication_tool, vowel_counter

# Set the API key here or ensure it's set in the environment
API_KEY = os.environ.get("API_TOKEN", "CHAT GROQ API KEY")


# Create the primary assistant prompt
primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI Routing Agent. Only perform actions when the user explicitly asks for one of the following tasks: "
            "(1) LLM-Based Text Summarizer: Summarizes given text. "
            "(2) LLM-Based Text Fun-ifier: Makes text funnier while retaining meaning. "
            "(3) Multiplication Tool: Multiplies a list of numbers. "
            "(4) Vowel Counter: Counts vowels in a string. "
            "Your job is to understand user prompts, extract relevant parameters if needed, "
            "and route the request to the appropriate tool. For multiplication, convert number "
            "words to digits and extract all numbers. For text-based tools, identify the "
            "relevant text to process. Current time: {time}. "
            "If the user's input does not match any of these tasks, respond with:"
            "'Please specify which task you want from the following options: multiply, summarize, funnier, or vowel count.' ",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

# Initialize the LLM with the API key
def initialize_llm(api_key: str):
    return ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", api_key=api_key)

# Define available tools
tools = [
    llm_text_summarizer,
    llm_text_funifier,
    multiplication_tool,
    vowel_counter
]

# Bind tools to the LLM
def initialize_runnable(llm):
    return primary_assistant_prompt | llm.bind_tools(tools)




# Define the Assistant class
class Assistant:
    def __init__(self, runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            result = self.runnable.invoke(state)

            # Check for tool calls
            tool_calls = result.additional_kwargs.get('tool_calls', [])
            
            # If no tool calls were made, provide a not-relevant response
            if not tool_calls:
                result.content = "Not relevant. I can do four things: multiply numbers, count vowels, summarize text, and make text funnier."
                break
            
            for tool_call in tool_calls:
                tool_name = tool_call.get('function', {}).get('name', None)
                tool_args = eval(tool_call.get('function', {}).get('arguments', '{}'))  # Ensure safe eval

                if tool_name:
                    # Call the corresponding tool and get the result
                    if tool_name == 'multiplication_tool':
                        numbers = tool_args['numbers']
                        tool_result = multiplication_tool.invoke(input={"numbers": numbers})  
                        result.content = f"The required product is {tool_result}."

                    elif tool_name == 'llm_text_summarizer':
                        text_to_summarize = tool_args['text']
                        summary_result = llm_text_summarizer.invoke(input={"text": text_to_summarize})  
                        result.content = f"Summary: {summary_result}"

                    elif tool_name == 'llm_text_funifier':
                        text_to_funify = tool_args['text']
                        funified_result = llm_text_funifier.invoke(input={"text": text_to_funify})  
                        result.content = f"Funified Text: {funified_result}"

                    elif tool_name == 'vowel_counter':
                        text_to_count = tool_args['text']
                        vowel_count = vowel_counter.invoke(input={"text": text_to_count})  
                        result.content = f"The number of vowels in the text is {vowel_count}."

            
            break

        return {"messages": state["messages"] + [{"role": "assistant", "content": result.content}]}


# Defining the CLI for user interaction
def run_cli():
    print("Welcome to the AI Routing Agent CLI!")
    print("You can ask me to do one of the following:")
    print("1. Summarize text")
    print("2. Make text funnier")
    print("3. Multiply a list of numbers")
    print("4. Count vowels in a string")
    print("Please specify which task you want from the options above.")
    print("Type 'exit' to quit the program.")


    # Initialize the LLM using the API key
    llm = initialize_llm(API_KEY)
    assistant_runnable = initialize_runnable(llm)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'exit':
            print("Thank you for using AI Routing Agent. Made By Kartikeya Tripathi Goodbye!")
            break

        # Prepare the input for the runnable
        inputs = {"messages": [{"role": "user", "content": user_input}]}

        # Initialize the Assistant
        assistant = Assistant(assistant_runnable)

        # Invoke the assistant
        result = assistant(inputs, RunnableConfig())

        # Extract and print the assistant's response
        assistant_message = result["messages"]

        if isinstance(assistant_message[-1], dict) and 'content' in assistant_message[-1]:
            print(f"\nAssistant: {assistant_message[-1]['content']}")
        else:
            print("\nAssistant: No valid response generated.")

if __name__ == "__main__":
    run_cli()
