import os
from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncOpenAI
from tools import web_search
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment config (set your key in .env or directly)
token = os.getenv("OPENAI_KEY")

client = AsyncOpenAI(api_key=token)
set_tracing_disabled(True)

model_instance = OpenAIChatCompletionsModel(
    model="gpt-4o",  # or "gpt-3.5-turbo" if preferred
    openai_client=client
)

agent = Agent(
    name="Web Search Chatbot",
    instructions="""
    You are a helpful assistant. If you do not know the answer to a user's question, 
    use the 'web_search' tool to search online for an answer. Respond only if you're confident.
    """,
    model=model_instance,
    model_settings=ModelSettings(temperature=0.3),
    tools=[web_search]
)

async def run_agent(user_input: str):
    result = await Runner.run(agent, user_input)
    return result.final_output