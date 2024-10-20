import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

st.title(":robot_face:🔗 TaraBot")
st.caption(":green[A LangChain App by Tara]")
st.caption("Remember, every AI model gives false or inaccurate information sometimes.")

zone = "USDA Agricultural Zone 8b"

def generate_response(input_text):
   # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
   llm = ChatOllama(
      model = "llama3.1:latest",
      temperature = 0.8,
      num_predict = 256,
    # other params ...
    )
   
   #System message to guide AI behavior
   messages = [
       ("system", "You are a helpful expert gardener in {zone}"),
       ("human", input_text)
       ]
   chat_message = llm.invoke(messages)
   st.success(chat_message.content)
   #st.info(chat_message.response_metadata)
   #st.info(llm(input_text))

# Main Chat Block
with st.form("my_form"):
    text = st.text_area(label="Ask away!")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

st.divider()

