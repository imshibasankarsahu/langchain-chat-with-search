# 🧠 LangChain Web Search Chatbot (Day 10/30 – GenAI Challenge)

This project is part of my **30-day GenAI Real-World Challenge**. It's a chatbot powered by **LangChain Agents**, using **Groq's Gemma2-9b-it LLM** and tools like **Arxiv**, **Wikipedia**, and **DuckDuckGo** for real-time search capabilities.

## 🔍 Features
- Natural language interface with `streamlit`
- Real-time search using:
  - 🦆 DuckDuckGo
  - 📚 Arxiv academic papers
  - 🌐 Wikipedia
- Fast and intelligent responses using Groq's LLM (`Gemma2-9b-it`)
- Interactive chat interface via `st.chat_input()` and `st.chat_message()`

## 📁 File Structure

```
project32/
├── project32.py         # Main Streamlit app
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## ▶️ How to Run

1. **Clone the repo**:
```bash
git clone https://github.com/your-username/project32.git
cd project32
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up `.env` file**:
Create a `.env` file and add your Groq API key:
```env
HF_TOKEN=your_huggingface_token
```

4. **Run the app**:
```bash
streamlit run project32.py
```

## 🛠 Dependencies

- `langchain`
- `langchain-community`
- `langchain-groq`
- `streamlit`
- `python-dotenv`
- `duckduckgo-search`



## 🚀 Credits
Built by [shiba sankar sahu] as part of the 30-Day GenAI Challenge 💥

---

### 📄 License
MIT
