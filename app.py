import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set up API key from Streamlit secrets
import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Initialize LLM once
if "llm" not in st.session_state:
    st.session_state.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("💬 Gemini Chatbot")

# Input box for user prompt
user_input = st.text_input("You:", key="input")

# When user submits input
if user_input:
    if user_input.lower().strip() == "quit":
        st.write(" Exiting chat.")
    else:
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        try:
            # Get response from model
            result = st.session_state.llm.invoke(st.session_state.chat_history)
            response = result.content

            # Display and store AI response
            st.session_state.chat_history.append(AIMessage(content=response))
            st.write(f"**AI:** {response}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display previous conversation
if st.session_state.chat_history:
    with st.expander("🔁 Conversation History", expanded=False):
        for msg in st.session_state.chat_history:
            if isinstance(msg, HumanMessage):
                st.markdown(f"**You:** {msg.content}")
            elif isinstance(msg, AIMessage):
                st.markdown(f"**AI:** {msg.content}")
