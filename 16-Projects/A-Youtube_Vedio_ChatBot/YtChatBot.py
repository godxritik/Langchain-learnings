from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utilities import extract_video_id, format_documents
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


video_url = input("Enter the YouTube video URL: ")

# 1. Extract Video Id from Video URL
video_id = extract_video_id(video_url)
print(f"Extracted Video ID: {video_id}")

# 2. Loading Transcript of the video from api
try:
    transcript_api = YouTubeTranscriptApi()
    transcript_list = transcript_api.fetch(video_id, languages=["en","hi"])
    # creating flattened format of transcript list
    transcript = " ".join([chunk.text for chunk in transcript_list])

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")

# 3. Setting up embedding model (using local model lm-studio)
embedding_model = OpenAIEmbeddings(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="text-embedding-bge-m3",
    check_embedding_ctx_length=False
)


# 4. Text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# trying out semantic text splitter
# text_splitter = SemanticChunker(
#     embeddings=embedding_model,
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1,
# )

text_chunks = text_splitter.create_documents([transcript])
print("No. of chunks created = ", len(text_chunks))


# Creating vector store from chunks
vector_store = Chroma.from_documents(text_chunks,embedding=embedding_model)

# 5 Creating a Retriever to search for similar chunks
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k":5
    }
)

# 6. Creating a Chat model instance for query answering
chat_model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="google/gemma-4-e2b",
    temperature=0
)

# 7. Formulating a prompt that combines the user query and retrieved documents from vector store
prompt = PromptTemplate(
    template=
    """
    You are a helpful assistant.
    Answer the query from the transcript context provided to you.
    If the context is insufficient to answer just say insufficient context
    
     **Context**
    {context}
    
    **Query**
    {query}

    """,
    input_variables=["context", "query"]
)

# 8. Creating a parser to parse output from llm
parser = StrOutputParser()

# 9. Creating a chain pipeline
parallel_chain = RunnableParallel({
    "context" : retriever | RunnableLambda(format_documents),
    "query" : RunnablePassthrough()
})

main_chain = parallel_chain | prompt | chat_model | parser

# 10. invoking the pipeline to get final output
final_answer = main_chain.invoke("what is machine learning?")

print(final_answer)
