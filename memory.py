from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
load_dotenv()

db= SqliteDb(db_file= "agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db= db,
        model= Groq(id="qwen/qwen3-32b"),
        markdown= True,
        add_history_to_context= True,
    )

openai_agent = build_agent()
openai_agent.print_response("What is the capital of France?")
openai_agent.print_response("What is the best time to visit it?")