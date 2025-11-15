# Local AI Chatbot (Ollama + Python + Streamlit)

A simple local AI chatbot built using **Ollama**, **Python**, and **Streamlit**.  
Runs fully offline using local LLMs such as **Phi-3**.

---

## Features

- Runs completely locally (no cloud required)
- Streamlit web interface
- Works with any Ollama model (e.g., phi3, llama3, etc.)
- Simple and lightweight setup

---

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```
### 2. Install dependencies

Using requirements file:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit requests
```
## Setup Ollama

### 3. Install Ollama

Download from: https://ollama.com/download

### 4. Pull and run a model (example: Phi-3)
```bash
ollama run phi3
```

Leave Ollama running in the background.

## Run the Chatbot

Inside the project folder:
```bash
streamlit run chatbot.py
```

Open the local URL and start chatting.

## License

MIT License. See `LICENSE.md` for details.
Copyright © 2025 Tanvi V R Medapati.
