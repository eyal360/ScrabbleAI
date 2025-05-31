from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash", # https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash
    description="A built in tool to look up for stuff using google search",
    instruction="""
        You are a helpful assistant that can use the following tools:
        - google_search 
    """,
    tools=[google_search],
)




