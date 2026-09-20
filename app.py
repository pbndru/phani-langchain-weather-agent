import os
from typing import Any

from langchain.agents import AgentType, initialize_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "google/gemma-4-e4b")


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def build_agent() -> Any:
    local_model = ChatOpenAI(
        base_url=LM_STUDIO_BASE_URL,
        api_key=LM_STUDIO_API_KEY,
        model=LM_STUDIO_MODEL,
        temperature=0,
        timeout=30,
    )

    return initialize_agent(
        tools=[get_weather],
        llm=local_model,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs={"system_message": "You are a helpful assistant"},
        verbose=False,
    )


def main() -> None:
    agent = build_agent()
    result = agent.invoke(
        {"input": "What's the weather in San Francisco?"}
    )
    print(result["output"])


if __name__ == "__main__":
    main()
