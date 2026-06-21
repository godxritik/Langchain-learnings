from  langchain_google_genai import ChatGoogleGenerativeAI
import dotenv
import  streamlit as st

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

st.header("My Research Paper App")

user_input = st.text_input("enter your input here")

if st.button("Ask Gemini"):
    response = model.invoke(user_input)
    st.write(response.content)



