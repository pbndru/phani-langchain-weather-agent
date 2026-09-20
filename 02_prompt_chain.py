import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "google/gemma-4-e4b")


def main() -> None:
    model = ChatOpenAI(
        base_url=LM_STUDIO_BASE_URL,
        api_key=LM_STUDIO_API_KEY,
        model=LM_STUDIO_MODEL,
        temperature=0,
        timeout=30,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a patient programming tutor."),
            (
                "human",
                "Explain {topic} for a beginner in three bullet points.",
            ),
        ]
    )

    chain = prompt | model | StrOutputParser()
    response = chain.invoke({"topic": "LangChain prompt templates"})
    print(response)


if __name__ == "__main__":
    main()
