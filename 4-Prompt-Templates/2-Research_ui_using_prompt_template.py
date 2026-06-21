from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

st.header("Research Paper App with Prompt Template")

paper_name = st.selectbox("select your research paper",["Attention is all you need", "Word2Vec", "ImageNet Classification with Deep Convolutional Neural Networks (2012)", "Deep Residual Learning for Image Recognition (2015)","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)"])

explanation_type = st.selectbox("select your explanation type",["beginner-friendly","technical", "highly-technical", "implementation-focused", "real-world analogy based", "researcher-focused"])

word_count = st.selectbox("select the length of the  summary", ["100", "200", "300", "500", "700+"])

prompt_template = PromptTemplate(
    template=""" You are an expert AI researcher and technical writer.

Read and analyze the research paper titled:

**Paper Title:** {paper_name}

Create a "{explanation_type}" summary of approximately **{word_count} words**.

Requirements:

1. Explain the main problem the paper aims to solve.
2. Describe the proposed methodology or architecture.
3. Highlight the key innovations and contributions.
4. Summarize the experiments, datasets, and evaluation metrics used.
5. Present the most important results and findings.
6. Explain why this paper is significant and its impact on the field.
7. Use clear, accurate language appropriate for a {explanation_type} audience.
8. Preserve important technical details, equations, model names, and terminology where relevant.
9. Do not copy large portions of the paper verbatim; paraphrase and explain the concepts.
10. Structure the response with the following sections:

* Overview
* Problem Statement
* Proposed Approach
* Key Contributions
* Experimental Results
* Limitations (if mentioned)
* Impact and Applications
* Conclusion

Ensure the final summary is approximately {word_count} words and maintains technical accuracy.
 """,
    input_variables = ["paper_name", "explanation_type", "word_count"]
)

prompt = prompt_template.invoke({
    "paper_name": paper_name,
    "explanation_type": explanation_type,
    "word_count": word_count
})

if st.button("explain"):
    response = model.invoke(prompt)
    st.write(response.content)



