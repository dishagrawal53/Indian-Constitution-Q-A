import gradio as gr
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Load FAISS retriever
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(".", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

def respond(
    message,
    history,
    system_message,
    max_tokens,
    temperature,
    top_p,
):
    """
    RAG-enhanced chatbot that retrieves relevant constitutional text before generating answers.
    """
    # Retrieve relevant context from FAISS
    try:
        docs = retriever.invoke(message)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        enhanced_system_message = f"""{system_message}
You are an expert on the Constitution of India. Use the following relevant constitutional text to answer the user's question:
CONSTITUTIONAL CONTEXT:
{context}
Provide a clear, accurate answer based on this context. Cite specific articles when relevant."""
        
    except Exception as e:
        enhanced_system_message = system_message
    
    # Get token from Space secret
    hf_token = os.getenv("HF_TOKEN")
    
    # Generate response using InferenceClient
    client = InferenceClient(token=hf_token, model="Qwen/Qwen2.5-72B-Instruct")
    
    messages = [{"role": "system", "content": enhanced_system_message}]
    
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})
    
    response = ""
    try:
        for msg in client.chat_completion(
            messages,
            max_tokens=max_tokens,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        ):
            if msg.choices and msg.choices[0].delta.content:
                response += msg.choices[0].delta.content
            yield response
    except Exception as e:
        yield f"Error: {str(e)}\n\nShowing retrieved context instead:\n\n{context[:1000]}"

# Create Gradio ChatInterface
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(
            value="You are an expert legal assistant specializing in the Constitution of India. Provide clear, accurate, and helpful answers.",
            label="System message",
            lines=3
        ),
        gr.Slider(minimum=256, maximum=2048, value=1024, step=64, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
        ),
    ],
    title="📜 Ask the Constitution of India",
    description="""
    Get intelligent answers about the Indian Constitution powered by RAG (Retrieval-Augmented Generation).
    
    The system retrieves relevant constitutional text and uses AI to provide clear, accurate explanations.
    """,
    examples=[
        ["What is Article 370?"],
        ["Explain fundamental rights in simple terms"],
        ["What does Article 21 say?"],
        ["What are directive principles?"],
    ],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch()