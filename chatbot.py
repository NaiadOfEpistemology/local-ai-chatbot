import streamlit as st
import requests
import json

st.set_page_config(page_title="why are you looking at this?", layout="centered")
st.title("tanvi's little... assistant")
st.caption("made him using ollama")

if "chat" not in st.session_state:
    st.session_state.chat=[]

for msg in st.session_state.chat:
    st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")

prompt=st.text_input("You:")

def get_response(prompt):
    try:
        url="http://localhost:11434/api/generate"
        payload={"model":"phi3","prompt":prompt}
        with requests.post(url,json=payload,stream=True,timeout=60) as r:
            full_reply=""
            for line in r.iter_lines():
                if not line:
                    continue
                try:
                    data=json.loads(line.decode("utf-8").replace("data: ",""))
                    if "response" in data:
                        full_reply+=data["response"]
                except json.JSONDecodeError:
                    continue
            return full_reply.strip() if full_reply else "⚠️ No reply from model."
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
        reply=get_response(prompt)
    st.session_state.chat.append({"role":"assistant","content":reply})
    st.rerun()

if clear:
    st.session_state.chat=[]
    st.rerun()
