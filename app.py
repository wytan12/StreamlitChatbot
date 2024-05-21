import streamlit as st
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

## Initialize LLM using AzureChatOpenAI
llm = AzureChatOpenAI(
    openai_api_version=st.secrets["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],
    api_key=st.secrets["AZURE_OPENAI_APIKEY"],
    azure_deployment=st.secrets["DEPLOYMENT_NAME"],
    temperature=1
)

st.set_page_config(page_title= "ChatBot", page_icon=":books:")

with st.sidebar:
    st.header("Profile")
    # st.subheader("This is a subheader")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    gender = st.radio(
        label = "Gender",
        options = ("Male", "Female")
    )
    if gender == "Male":
        st.header("Welcome Guys :boy:")
    else:
        st.header("Welcome Girls :girl:")

st.title(":books: AskNarelle")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Tell me something...")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role":"user", "content": prompt})

    # Prepare messages for AzureChatOpenAI
    chat_history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    # Call AzureChatOpenAI
    ai_message = llm.invoke(chat_history)
   
    # Extract the response content
    full_response = ai_message.content

    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})


