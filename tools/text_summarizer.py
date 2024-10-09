from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class TextSummarizer:
    def __init__(self):
        self.llm = OpenAI(temperature=0.3)
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following text:\n\n{text}\n\nSummary:"
        )

    def summarize(self, text: str) -> str:
        return self.llm(self.prompt.format(text=text))
