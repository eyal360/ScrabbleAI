from google.adk.agents import Agent
from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Tools must return JSON-serializable data
    }

root_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash", # https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash
    description="A custom tool to get the current time",
    instruction="""
        You are a helpful assistant that can use the following tools:
        - get_current_time
    """,
    tools=[get_current_time],
)




