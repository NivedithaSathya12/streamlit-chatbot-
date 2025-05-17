import streamlit as st
import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Set API key
import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("💬 Chat with Gemini 2.0 Flash")
st.caption("Built with Streamlit and LangChain")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Input box for user
user_input = st.chat_input("Say something...")

if user_input:
    # Add human message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Get AI response
    response = llm.invoke(st.session_state.chat_history)
    
    # Add AI response to chat history
    st.session_state.chat_history.append(AIMessage(content=response.content))

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)
