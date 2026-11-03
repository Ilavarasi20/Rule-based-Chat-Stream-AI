import streamlit as st

# Page configuration
st.set_page_config(
    page_title="ChatStream AI",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #E6D6F5 !important;
    color: #000000 !important;
}

/* Header */
[data-testid="stHeader"] {
    background-color: #E6D6F5 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #21113D !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Main headings */
h1, h2, h3, p, label {
    color: #4B286D !important;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background-color: #F8DFFF;
    border: 1px solid #E6B8F2;
    border-radius: 18px;
    padding: 15px;
    margin-bottom: 12px;
}

/* Input box */
[data-testid="stChatInput"] {
    background-color: white !important;
    border: 2px solid #D8A5F3 !important;
    border-radius: 20px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #7026B9, #A044D5);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #54158C;
    color: white !important;
}

/* Divider */
hr {
    border-color: #D9B4E8;
}

</style>
""", unsafe_allow_html=True)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm ChatStream AI! How can I help you today?"
        }
    ]


# Chatbot response function
def chatbot_response(user_input):

    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey", "hai"]:
        return "Hi! 😊 How are you today?"
    elif "i am good" in message:
            return "Happy to hear💜"
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. 💜"

    elif "your name" in message:
        return "I'm ChatStream AI, your friendly chatbot! 🤖"

    elif "what can you do" in message:
        return "I can answer questions, tell jokes, explain concepts and help you learn! ✨"

    elif "python" in message:
        return "Python is a popular, beginner-friendly programming language. 🐍"

    elif "joke" in message:
        return "Why did the computer catch a cold? Because someone left its Windows open! 😂"

    elif "thankyou" in message:
        return "You're always welcome! 💜"

    elif message in ["bye", "goodbye"]:
        return "Goodbye! Have a wonderful day! 👋"

    else:
        return "Sorry, I don't understand that yet. Can you ask me something else? 😊"


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("<h1 style='text-align:center;'>🤖</h1>",
                unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align:center;color:white;'>ChatStream AI</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#E5C9FF;'>Ask • Learn • Explore</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 💬 Navigation")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! 👋 I'm ChatStream AI! How can I help you today?"
            }
        ]
        st.rerun()

    if st.button("ℹ️ About", use_container_width=True):
        st.session_state.show_about = not st.session_state.get(
            "show_about", False
        )

    if st.button("✨ Features", use_container_width=True):
        st.info("Greetings, questions, jokes and fallback responses!")

    st.divider()

    st.markdown(
        "<p style='text-align:center;'>✨ Your AI Companion"
        "<br>for a Smarter Tomorrow ✨</p>",
        unsafe_allow_html=True
    )


# ---------------- MAIN PAGE ----------------

col1, col2 = st.columns([2, 4])

with col1:
    st.image("bot.jpg", width=200)

with col2:
    st.title("ChatStream AI")
    st.markdown("### Smart Chat. Endless Possibilities.")

st.divider()

# Online status
st.markdown("🟢 **Online**")

# About section
if st.session_state.get("show_about", False):
    st.info(
        "ChatStream AI is a simple rule-based chatbot "
        "developed using Python and Streamlit. "
        "It responds to predefined user inputs."
    )

# Welcome message
st.markdown("### 💜 Welcome to ChatStream AI!")

st.write("Your friendly assistant is ready to chat with you.")

st.divider()

# Display previous messages
for msg in st.session_state.messages:

    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])

    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])


# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Save human message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Generate chatbot response
    response = chatbot_response(user_input)

    # Save chatbot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
