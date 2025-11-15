import streamlit as st
import requests
import json
st.markdown("""
<style>

* {
    font-family: "Comic Sans MS", "Comic Sans", cursive !important;
    color: #b30047 !important; /* dark cherry pink text */
}
body, .main, .stApp {
    background: #ffffff !important; 
}
.chat-bubble-user {
    background: #ff4d88;
    color: white !important;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    max-width: 80%;
    margin-left: auto;
}
.chat-bubble-assistant {
    background: #ffe4ef;
    color: #b30047 !important; 
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    max-width: 80%;
    margin-right: auto;
    border: 1px solid #ff4d88;
}
.stTextInput>div>div>input {
    background: #ffffff !important;  /* white text field */
    color: #b30047 !important;       /* dark cherry pink text */
    border: 2px solid #ff4d88 !important;
    border-radius: 10px !important;
    padding: 8px !important;
    font-size: 16px !important;
}
.stButton>button {
    background-color: #ff4d88 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 8px 16px !important;
    border: none !important;
}

.stButton>button:hover {
    background-color: #b30047 !important;
}
footer, #MainMenu, header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="why are you looking at this?", layout="centered")
st.title("tanvi's little... assistant")
st.caption("made him using ollama")
if "chat" not in st.session_state:
    st.session_state.chat=[]

for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-assistant'>{msg['content']}</div>", unsafe_allow_html=True)



prompt=st.text_input("you:")

def get_response():
    try:
        url="http://localhost:11434/api/chat"
        payload={
            "model":"phi3",
            "messages":st.session_state.chat[-12:]
        }

        with requests.post(url,json=payload,stream=True,timeout=120) as r:
            reply=""
            for line in r.iter_lines():
                if not line:
                    continue
                try:
                    chunk=line.decode("utf-8").replace("data: ","")
                    data=json.loads(chunk)
                    if "message" in data and "content" in data["message"]:
                        reply+=data["message"]["content"]
                except:
                    continue

        return reply.strip() if reply else "no reply from model."

    except Exception as e:
        return f"you messed up: {e}"

col1,col2=st.columns([3,1])
with col1:
    send=st.button("send")
with col2:
    clear=st.button("clear chat")
if send and prompt:
    st.session_state.chat.append({"role":"user","content":prompt})
    with st.spinner("i'm thinking..."):
        reply=get_response()
    st.session_state.chat.append({"role":"assistant","content":reply})
    st.rerun()
if clear:
    st.session_state.chat=[]
    st.rerun()
