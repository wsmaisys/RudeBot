import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid

# VS Code-inspired theme
st.markdown("""
    <style>
        /* Overall background and text colors */
        .stApp {
            background-color: #1e1e1e;
            color: #d4d4d4;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #252526;
        }
        
        /* Chat message containers - removed background */
        .stChatMessage {
            background-color: transparent !important;
            border: none !important;
            padding: 0.25rem !important;
        }
        
        /* Input box styling */
        .stTextInput input {
            background-color: #3c3c3c;
            color: #d4d4d4;
            border: 1px solid #404040;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: #0e639c;
            color: #ffffff;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1177bb;
        }
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 10px;
            background-color: #1e1e1e;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #424242;
        }
        
        /* Caption styling */
        .st-caption {
            color: #858585;
        }
    </style>
""", unsafe_allow_html=True)

# **************************************** utility functions *************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']


# **************************************** Session Setup ******************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])


# **************************************** Sidebar UI *********************************

st.sidebar.title('😈 RudeBot')

if st.sidebar.button('🔄 New Chat'):
    reset_chat()

st.sidebar.header('💬 My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages


# **************************************** Main UI ************************************

# Add centered heading and disclaimer
st.markdown("<h1 style='text-align: center;'>😈 RudeBot </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #858585; font-size: 0.9em; margin-bottom: 20px;'>⚠️ Disclaimer: RudeBot is created for entertainment purposes only. Please don't get offended - it's all in good fun!</p>", unsafe_allow_html=True)

# Add some space after the headers
st.markdown("<br>", unsafe_allow_html=True)

# loading the conversation history
for message in st.session_state['message_history']:
    if message['role'] == 'assistant':
        st.write(f"😈 {message['content']}")
    else:
        st.write(f"🧑 You: {message['content']}")

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    st.write(f"🧑 You: {user_input}")

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    # Show a simple loading message while generating
    loading_placeholder = st.empty()
    loading_placeholder.write("😈 thinking...")
    
    # Get AI response
    response_container = st.empty()
    response = ""
    for message_chunk, metadata in chatbot.stream(
        {'messages': [HumanMessage(content=user_input)]},
        config=CONFIG,
        stream_mode='messages'
    ):
        response += message_chunk.content
        response_container.write(f"😈 {response}")

    # Remove the loading message
    loading_placeholder.empty()

    # Add to message history
    st.session_state['message_history'].append({'role': 'assistant', 'content': response})