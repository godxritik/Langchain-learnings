from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

st.header("Research Paper App with Prompt Template")

paper_name = st.selectbox("select your research paper",["Attention is all you need", "Word2Vec", "ImageNet Classification with Deep Convolutional Neural Networks (2012)", "Deep Residual Learning for Image Recognition (2015)","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)"])

explanation_type = st.selectbox("select your explanation type",["beginner-friendly","technical", "highly-technical", "implementation-focused", "real-world analogy based", "researcher-focused"])

word_count = st.selectbox("select the length of the  summary", ["100", "200", "300", "500", "700+"])

prompt_template = load_prompt("research_paper_prompt_template.json")

prompt = prompt_template.invoke({
    "paper_name": paper_name,
    "explanation_type": explanation_type,
    "word_count": word_count
})

if st.button("explain"):
    response = model.invoke(prompt)
    st.write(response.content)



