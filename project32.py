import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import initialize_agent,AgentType
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")

arxiv_warp=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=300)
wiki_wrap=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=300)
arxiv=ArxivQueryRun(api_wrapper=arxiv_warp)
wiki=WikipediaQueryRun(api_wrapper=wiki_wrap)
search=DuckDuckGoSearchRun(description="search on the web",name='search')

#streamlit app

st.title("langchain chat with search")

st.sidebar.title("settings")
api_key=st.sidebar.text_input("Enter your api key",type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"I am  a chatbot assistant i can search on web"}
    ]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="what is machine learning"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=api_key,model="Gemma2-9b-It",streaming=True)
    tool=[arxiv,wiki,search]
    agent=initialize_agent(
        tools=tool,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handling_parsing_errors=True
        
    )
    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)
