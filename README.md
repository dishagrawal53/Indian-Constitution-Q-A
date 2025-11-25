<h1 align="center"> Constitution of India – RAG Chatbot</h1>

<p align="center">
  <strong>An AI-powered Retrieval-Augmented Generation (RAG) chatbot built using FAISS, MiniLM embeddings, and a large language model.</strong>
</p>

<p align="center">
   <a href="https://huggingface.co/spaces/itsmedi/constitution"><strong>Live Demo (Hugging Face Spaces)</strong></a>
</p>

<hr/>

<h2> Overview</h2>

<p>
This project is an intelligent chatbot that answers questions about the <strong>Constitution of India</strong> using a 
Retrieval-Augmented Generation (RAG) pipeline. It retrieves the most relevant constitutional text from a 
FAISS vector index and sends the enriched context to a strong instruction-tuned language model hosted on Hugging Face.
</p>

<p>
The goal is to provide <strong>clear, accurate, article-based responses</strong> about constitutional concepts, fundamental rights, duties, amendments, and more — all through a simple Gradio interface.
</p>

<hr/>

<h2> File Structure</h2>

<pre>
Root Directory
│
├── app.py                 → Gradio RAG chatbot that loads FAISS and answers queries
├── vector_generator.ipynb → Notebook used to generate the FAISS index from the Constitution PDF
│
├── index.faiss            → FAISS vector index (embeddings)
├── index.pkl              → Metadata for vector index
│
└── README.md              → Documentation (this file)
</pre>

<hr/>

<h2>🔍 How It Works</h2>

<ul>
  <li><strong>1. Text Extraction & Chunking:</strong> The Constitution PDF is loaded and split into overlapping text chunks.</li>
  <li><strong>2. Embedding Generation:</strong> Each chunk is converted into embeddings using 
      <code>sentence-transformers/all-MiniLM-L6-v2</code>.</li>
  <li><strong>3. FAISS Index Creation:</strong> All embeddings are stored in a FAISS vector store for efficient similarity search.</li>
  <li><strong>4. Query Processing:</strong> When a user asks a question, relevant chunks are retrieved using vector similarity.</li>
  <li><strong>5. RAG Response:</strong> Retrieved context is merged into the system prompt and sent to an LLM 
      (Qwen2.5-72B-Instruct).</li>
  <li><strong>6. Gradio UI:</strong> Users interact with a simple chat interface to ask constitutional questions.</li>
</ul>

<hr/>

<h2>🚀 Features</h2>

<ul>
  <li> Retrieval-Augmented Generation for accurate, context-driven answers</li>
  <li> FAISS vector search over the full Constitution of India</li>
  <li> Automatic retrieval of relevant Articles, Parts, and clauses</li>
  <li> LLM-powered responses with citations when appropriate</li>
  <li>Gradio Chat UI with system prompts, temperature, top-p controls</li>
  <li> Notebook included for regenerating FAISS index any time</li>
  <li>Fully deployable on Hugging Face Spaces</li>
</ul>

<hr/>

<h2> Files Explained</h2>

<h3><code>vector_generator.ipynb</code></h3>
<p>
This Jupyter notebook handles the creation of the FAISS index.  
It performs PDF loading, text chunking, embedding generation, and saving of:
</p>

<ul>
  <li><code>index.faiss</code></li>
  <li><code>index.pkl</code></li>
</ul>

<p>It is designed to run easily on platforms like <strong>Kaggle</strong>.</p>

<h3> <code>app.py</code></h3>
<p>
The main Gradio application.  
It loads the FAISS vector store, retrieves the most relevant text for each query, and sends it to the LLM along with a custom system prompt.
</p>

<p>The app uses:</p>
<ul>
  <li>FAISS retriever</li>
  <li>MiniLM embeddings</li>
  <li>Hugging Face Inference API</li>
  <li>Gradio ChatInterface</li>
</ul>

<hr/>

<h2>Usage</h2>

<p>To run the chatbot locally:</p>

<ol>
  <li>Install dependencies from <code>requirements.txt</code></li>
  <li>Place <code>index.faiss</code> and <code>index.pkl</code> in the project root</li>
  <li>Set your Hugging Face API token as <code>HF_TOKEN</code></li>
  <li>Run <code>python app.py</code></li>
</ol>

<p>This will start the Gradio interface on <code>http://localhost:7860</code>.</p>

<hr/>

<h2>Deployment (Hugging Face Spaces)</h2>



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
  <li>LangChain & FAISS</li>
  <li>Gradio UI Framework</li>
</ul>

<hr/>

<h3 align="center">Made with ❤️ to promote Constitutional Awareness & Learning</h3>
