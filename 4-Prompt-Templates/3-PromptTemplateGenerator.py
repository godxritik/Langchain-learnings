from langchain_core.prompts import PromptTemplate

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

prompt_template.save("research_paper_prompt_template.json")