# AI Routing Agent by KT.

AI Routing Agent is a command-line interface (CLI) application that uses an AI(LLM) to route user queries to appropriate tools for processing. It uses the LangChain library and the Groq LLM API to provide intelligent responses and perform various tasks.

## Features

- Intelligent routing of queries to the appropriate tool
- Text summarization
- Text "fun-ification"
- Number multiplication
- Vowel counting


## Prerequisites

- Python 3.7 or higher
- Groq API key

## Installation

1. Download the folder
   ```
   git clone 
   cd "path of the folder"
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Set up your Groq API key:
   - Modify the `AI_ROUTING_AGENT.py`, `tools\text_summarizer.py` and `tools\text_funifier.py` file and set the `API_KEY` variable directly:
     ```python
     API_KEY = "your_api_key_here"
     ```
   

## Usage

To run the Mycroft AI Routing Agent:

```
python ai_routing_agent.py
```

Once started, you can interact with the agent by typing your queries. The agent will route your query to the appropriate tool and provide a response.

To exit the program, type 'exit' at the prompt.

## Example Prompts

Here are some example prompts you can use to interact with the Mycroft AI Routing Agent:

1. Text Summarization:
   ```
   You: Please summarize the following text: "text"
   ```

2. Text Fun-ification:
   ```
   You: Make this text funnier: "Text"
   ```

3. Number Multiplication:
   ```
   You: Multiply these numbers: 5, 7, and 3
   ```

4. Vowel Counting:
   ```
   You: Count the vowels in this sentence: "The quick brown fox jumps over the lazy dog."
   ```



## Project Structure

```
Kartikeya_tripathi_mycroft/
├── ai_routing_agent.py
├── tools/
│   ├── __init__.py
│   ├── text_summarizer.py
│   ├── text_funifier.py
│   ├── multiplication_tool.py
│   └── vowel_counter.py
├── requirements.txt
└── README.md
```
## Flowchart

```
[Start]
   |
[User Input]
   |
[Process Input]
   |
[Determine Tool]
   ├──> [Text Summarization Tool]
   |          |
   |      [Output Result]
   |
   ├──> [Text Funifier Tool]
   |          |
   |      [Output Result]
   |
   ├──> [Multiplication Tool]
   |          |
   |      [Output Result]
   |
   └──> [Vowel Counter Tool]
              |
          [Output Result]
   |
[Display Result to User]
   |
[End]
```

## Assumptions and Design Decisions

1. **LLM Choice**: The project uses the Groq API with the "mixtral-8x7b-32768" model. This choice was made based on the model's capabilities and performance.

2. **Tool Implementation**: Tools are implemented as separate functions, allowing for easy expansion and modification of the available toolset.

3. **In-Memory State Management**: A simple in-memory checkpointer is used for state management. For production use, consider implementing a more robust solution.

4. **Error Handling**: Basic error handling is implemented. In a production environment, more comprehensive error handling and logging should be added.

5. **Security**: The code uses `eval()` for parsing tool arguments. In a production environment, a more secure method of parsing JSON should be implemented.

6. **Scalability**: The current implementation is designed for CLI use. For scaling to a web service or larger application, consider implementing proper request handling and concurrency management.

7. **Tool Routing**: The AI model is responsible for routing queries to the appropriate tool. This design allows for flexible and intelligent query handling but relies on the model's understanding and accuracy.



## Acknowledgments


- Generative AI is used as an support.
