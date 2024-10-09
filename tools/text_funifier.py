from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class TextFunifier:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Make the following text funnier while retaining its original meaning:\n\n{text}\n\nFunny version:"
        )

    def funify(self, text: str) -> str:
        return self.llm(self.prompt.format(text=text))
