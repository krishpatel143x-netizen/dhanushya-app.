import stremlit as stremlit
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

st.title("Dhanushya - Market Analyis")

#user imput
user_imput = st.text_area("Enter your market data / question:")

if st.button("Analyze")
    if user_imput:
        llm = ChatOpenAI(openai_api_keys="YOUR_OPENAI_API_KEY", temprerature=0)
        template = ChatPromptTemplate.from_template("Analyze this data: (data)")
        prompt = template.format_massages(data=user_imput)
        response = llm(prompt)
        st.write(response.content)
    else:
        st.warning("Plase enter some data to analyze.")
        