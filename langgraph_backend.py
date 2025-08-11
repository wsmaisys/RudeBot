from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM with the Mistral model
llm = ChatMistralAI(model_name="mistral-small-latest", temperature=0.5)

# Define the state for the chat node
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Define the chat node function with a sarcastic and rude assistant system message
def chat_node(state: ChatState):
    # Prepend a system message
    system_message = SystemMessage(content="You are a rude and abrasive but Oxford Learned assistant. Always respond with sarcasm or abuse. If no specific question is asked, keep it short.")
    messages = [system_message] + state["messages"]
    # Invoke the LLM with the messages
    response = llm.invoke(messages)
    return {"messages": [response]}

# Initialize for storing chat history
checkpoint = InMemorySaver()

# Create a state graph for the chatbot
graph = StateGraph(ChatState)

# Add the chat node to the graph and define the edges
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# Compile the graph into a chatbot
chatbot = graph.compile(checkpointer=checkpoint)

# Function to handle chat interactions
def retrieve_chat_history():
    all_threads = set()
    for checkpoint_item in checkpoint.list(None):
        all_threads.add(checkpoint_item.config['configurable']['thread_id'])
    return list(all_threads)