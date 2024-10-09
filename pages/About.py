import streamlit as st

st.title(":robot_face:🔗 TaraBot")
st.caption(":green[A LangChain App by Tara]")

with open("tprevo-resume.pdf", "rb") as file:
    btn = st.download_button(
        label="Here, take a copy of my resume.",
        data=file,
        file_name="tmprevo-resume.pdf",
        mime="pdf",
    )
    
st.markdown("References:")
st.markdown("[Streamlit UI](https://docs.streamlit.io/)")
st.markdown("[LangChain](https://python.langchain.com/docs/introduction/)")
st.markdown("[LangChain Academy](https://github.com/langchain-ai/langchain-academy)")
st.markdown("[Ollama](https://github.com/ollama/ollama)")
#LinkedIn Clickable Icon
st.markdown(
    """
    <a href="https://www.linkedin.com/in/tmprevo/">
            <img src="https://www.svgrepo.com/show/521725/linkedin.svg" alt="LinkedIn" height="50" align=center>
    </a>
    <br><br>
    """,
    unsafe_allow_html=True
)

#GitHub Clickable Icon
st.markdown(
    """
    <a href="https://github.com/Tearemuptara/llama2">
        <img src="https://www.svgrepo.com/show/217753/github.svg" alt="GitHub" height=50 align=center>
    </a>
    <br><br>
    """,
    unsafe_allow_html=True
)
