<h1 align="center"> Constitution of India – RAG Chatbot</h1>

<p align="center">
  <strong>An AI-powered Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FAISS, MiniLM embeddings, and a large language model.</strong>
</p>

<p align="center">
   <a href="https://huggingface.co/spaces/itsmedi/constitution"><strong>Live Demo (Hugging Face Spaces)</strong></a>
</p>

<hr/>

<h2> Overview</h2>

<p>
This project is an intelligent chatbot that answers questions about the <strong>Constitution of India</strong> using a Retrieval-Augmented Generation (RAG) architecture powered by <strong>LangChain</strong>. 
</p>

<p>
LangChain serves as the core framework that handles:
<ul>
  <li>Document Loading</li>
  <li>Text Splitting</li>
  <li>Embedding Generation</li>
  <li>FAISS Vector Store Creation</li>
  <li>Retriever Logic</li>
</ul>
</p>

<p>
The final system retrieves the most relevant constitutional text and passes it to an instruction-tuned LLM hosted on Hugging Face to generate clear, accurate, article-based answers.
</p>

<hr/>

<h2> File Structure</h2>

<pre>
Root Directory
│
├── app.py                 → Gradio RAG chatbot using LangChain retriever + HF Inference API
├── vector_generator.ipynb → Notebook for creating the FAISS index using LangChain utilities
│
├── index.faiss            → FAISS vector index (embeddings)
├── index.pkl              → Metadata for vector index
│
└── README.md              → Documentation (this file)
</pre>

<hr/>

<h2> How It Works</h2>

<ul>
  <li><strong>1. PDF Loading (LangChain):</strong> The Constitution PDF is loaded using LangChain’s <code>PyPDFLoader</code>.</li>

  <li><strong>2. Text Chunking (LangChain):</strong> The text is split into overlapping chunks using 
      <code>RecursiveCharacterTextSplitter</code> for optimal retrieval.</li>

  <li><strong>3. Embedding Generation (LangChain):</strong> Each chunk is converted into embeddings using 
      <code>HuggingFaceEmbeddings</code> (<code>MiniLM-L6-v2</code>).</li>

  <li><strong>4. FAISS Index Creation (LangChain):</strong> A FAISS vector store is built using 
      <code>FAISS.from_documents()</code> and saved for fast retrieval.</li>

  <li><strong>5. Query Retrieval (LangChain):</strong> A retriever is created using 
      <code>vectorstore.as_retriever()</code> to fetch the top relevant chunks.</li>

  <li><strong>6. RAG Response:</strong> Retrieved context is embedded into the system prompt and sent to a large model 
      (Qwen2.5-72B-Instruct) via Hugging Face Inference API.</li>

  <li><strong>7. Gradio Interface:</strong> The user interacts with a ChatInterface that streams model responses.</li>
</ul>

<hr/>

<h2> Features</h2>

<ul>
  <li>LangChain-based RAG pipeline</li>
  <li>FAISS vector search over the entire Constitution of India</li>
  <li>MiniLM embeddings for fast retrieval</li>
  <li>Accurate, context-driven answers with article references</li>
  <li>Gradio Chat UI with temperature, top-p, and max-token controls</li>
  <li>Notebook included for regenerating the FAISS index</li>
  <li>Fully deployable on Hugging Face Spaces</li>
</ul>

<hr/>

<h2> Files Explained</h2>

<h3><code>vector_generator.ipynb</code></h3>

<p>
A complete LangChain-based workflow for generating the FAISS vector index.  
It includes:
</p>

<ul>
  <li>Loading the Constitution PDF using <strong>PyPDFLoader</strong></li>
  <li>Chunking using <strong>RecursiveCharacterTextSplitter</strong></li>
  <li>Generating embeddings with <strong>HuggingFaceEmbeddings</strong></li>
  <li>Creating and saving a <strong>FAISS vector store</strong></li>
</ul>

<p>This notebook is optimized for platforms like <strong>Kaggle</strong>.</p>

<h3><code>app.py</code></h3>

<p>
The main Gradio application using LangChain for retrieval and Hugging Face for generation.  
It:
</p>

<ul>
  <li>Loads FAISS via LangChain</li>
  <li>Creates a retriever with <code>vectorstore.as_retriever()</code></li>
  <li>Retrieves relevant chunks for every user query</li>
  <li>Streams model output to the Gradio ChatInterface</li>
</ul>


<hr/>

<h2> Example Questions Users Can Ask</h2>

<ul>
  <li>What is Article 21?</li>
  <li>Explain Fundamental Rights in simple terms.</li>
  <li>What does Article 368 say about amendments?</li>
  <li>What are Directive Principles?</li>
  <li>What is the Preamble?</li>
</ul>

<hr/>

<h2>⭐ Acknowledgements</h2>

<ul>
  <li>The Constitution of India (Public Domain)</li>
  <li>Hugging Face – Inference API & Model Hosting</li>
  <li>LangChain Framework</li>
  <li>FAISS Vector Search Library</li>
  <li>Gradio UI Framework</li>
</ul>

<hr/>

<h3 align="center">Made with ❤️ to promote Constitutional Awareness & Learning</h3>
