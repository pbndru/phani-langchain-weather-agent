import os

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "google/gemma-4-e4b")


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def main() -> None:
    model = ChatOpenAI(
        base_url=LM_STUDIO_BASE_URL,
        api_key=LM_STUDIO_API_KEY,
        model=LM_STUDIO_MODEL,
        temperature=0,
        timeout=30,
    )

    tool_enabled_model = model.bind_tools([get_weather])
    messages = [HumanMessage(content="What is the weather in San Francisco?")]
    response = tool_enabled_model.invoke(messages)

    if not response.tool_calls:
        print("Model reply:")
        print(response.content)
        print("\nThis model did not emit a tool call for this prompt.")
        return

    tool_call = response.tool_calls[0]
    tool_result = get_weather.invoke(tool_call["args"])
    messages.extend(
        [
            response,
            ToolMessage(content=tool_result, tool_call_id=tool_call["id"]),
        ]
    )

    final_response = tool_enabled_model.invoke(messages)
    print(final_response.content)


if __name__ == "__main__":
    main()
