# 💬 Offline ChatGPT-like Chatbot
A lightweight, local chatbot prototype built using **Streamlit** and **Ollama** that runs large language models (LLMs) like `phi3`, `mistral`, or `llama3` **entirely on your machine** — no internet or OpenAI API required.
---
## 🛠️ How to Run This Chatbot
Follow the steps below to get the chatbot running locally on your system.

### ✅ Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/your-chatbot-repo.git
cd your-chatbot-repo
```
---
### ✅ Step 2: Install Python & Streamlit
Make sure Python is installed on your system.
- Download from: https://www.python.org/
Then install the required Python packages:
```bash
pip install streamlit requests
```
---
### ✅ Step 3: Install & Set Up Ollama
Download and install Ollama:
🔗 https://ollama.com
Then pull any of the available models:
```bash
ollama pull phi3
# or
ollama pull mistral
# or
ollama pull llama3
```
This may take a few minutes (models are 2–4GB in size).
---
### ✅ Step 4: Run the Chatbot
Run the Streamlit app:
```bash
streamlit run app.py
```
Visit `http://localhost:8501` in your browser to chat with the bot.
---
### ✅ Step 5: Customize the Assistant Prompt (Optional)
To change the assistant's tone or role, open the `prompt.py` file and edit the `system_prompt`:
```python
# prompt.py
system_prompt = "You are a helpful and friendly AI assistant. Answer clearly and concisely."
```
Update and save to apply changes instantly.
---
## 🧠 Features

- Fully offline chatbot (no API or internet required after setup)
- Supports multiple LLMs (phi3, mistral, llama3)
- Chat memory via `st.session_state`
- Streamlit-based interface with typing indicators and clear chat button

---

## 📌 Credits
Project built during the **"Build Your Own ChatGPT"** cohort by **Faiz Khatri** and **LetsUpgrade**. 
---
---
Feel free to ⭐ star this repo and contribute!
