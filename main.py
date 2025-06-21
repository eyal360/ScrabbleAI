import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from scrabble_agent.agent import scrabble_agent
from utils import add_user_query_to_history, call_agent_async

load_dotenv()

# Initialize In-Memory Session Service
session_service = InMemorySessionService()

# Define Initial State for the Session
initial_state = {
    "user_name": "Test User",
    "user_shifts": [],
}


async def main_async():
    
    APP_NAME = "ScrabbleAI"
    USER_ID = "scrabble_user_123"

    # Create a new session with initial state
    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )
    SESSION_ID = new_session.id
    print(f"Created new session: {SESSION_ID}")

    # Create a runner with the main scrabble agent
    runner = Runner(
        agent=scrabble_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # Interactive Conversation Loop
    print("\nWelcome to ScrabbleAI Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input(f"{initial_state['user_name']}: ")

        # Check if user wants to exit
        if any(word in user_input.lower() for word in ["exit", "quit"]):
            print("Ending conversation. Goodbye!")
            break

        # Update interaction history with the user's query
        add_user_query_to_history(
            session_service, APP_NAME, USER_ID, SESSION_ID, user_input
        )

        # Process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
