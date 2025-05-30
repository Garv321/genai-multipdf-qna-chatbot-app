
# GenAI MultiPDF QnA Chatbot App using ObjectBox & LLaMA3

A professional-grade, high-performance Question-Answering (QnA) chatbot built on **Generative AI** and **ObjectBox Vector Database**. This application is engineered to process and understand **multiple PDFs** simultaneously and respond to user queries with precision using the **Retrieval-Augmented Generation (RAG)** pipeline.

---

## 🧠 Project Overview

This project integrates **Meta's LLaMA3 (8B)** model with **ObjectBox vector search** to enable fast, relevant, and intelligent querying across a directory of PDF documents. Users can interactively ask questions about their uploaded files, and receive context-aware, natural language responses powered by **LangChain**, **Streamlit**, and **Groq's LLM API**.

---

## 🧩 Key Features

- ✅ Retrieval-Augmented Generation (RAG) Pipeline using **ObjectBox**
- ✅ Fast and memory-efficient document embeddings with **HuggingFace (MiniLM-L6-v2)**
- ✅ Supports querying across **multiple PDF documents**
- ✅ Real-time QnA through Streamlit UI
- ✅ Chunking with **RecursiveCharacterTextSplitter** for better semantic retrieval
- ✅ Seamless integration of LangChain components


- **Retrieval-Augmented Generation (RAG) Pipeline:**  
  Combines **ObjectBox-based vector retrieval** with generative AI for precise and contextually relevant answers.
- **Multi-PDF Ingestion:** Upload and process numerous PDFs for comprehensive knowledge coverage.
- **Generative AI Integration:** Utilizes powerful LLMs for contextual, coherent, and human-like answers.
- **Contextual Querying:** Maintains conversational context for follow-up questions.
- **Scalable Architecture:** Built on FastAPI for backend API and Streamlit for an interactive frontend UI.
- **Secure & Configurable:** Environment variable support for API keys and sensitive configurations.
- **Extensible:** Modular design for easy integration with other data sources or models.

---

## 🧱 Tech Stack

| Layer        | Technology                              |
|--------------|------------------------------------------|
| Backend      | Python, FastAPI (optional)               |
| Frontend     | Streamlit                                |
| Embeddings   | HuggingFace - all-MiniLM-L6-v2           |
| Vector Store | ObjectBox Vector Database                |
| LLM          | LLaMA3-8B-Instant via Groq API           |
| Frameworks   | LangChain, dotenv                        |

---

## 📁 Folder Structure

```
genai-multipdf-qna-chatbot-app/
│
├── us_census/                     # PDF documents directory
├── .env                           # Environment variables
├── app.py                         # Streamlit app (main file)
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/genai-multipdf-qna-chatbot-app.git
cd genai-multipdf-qna-chatbot-app
```

### 2. Install Dependencies

Create a virtual environment and install required libraries:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Environment Variables

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Add Your PDF Files

Place your PDF documents inside the `./us_census/` directory. You can rename or expand the folder as required.

---

## 🚀 Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Click the **"Documents Embedding"** button to ingest PDFs into ObjectBox vector DB.
2. Enter your natural language question in the prompt.
3. The app retrieves relevant document chunks and generates an answer using LLaMA3.

---

## 🎯 Use Cases

- Enterprise document search and support automation
- Legal and compliance document QnA
- Academic research assistant
- Customer support knowledge bases
- Any domain requiring scalable PDF document interaction via natural language

---

## 📈 Performance Highlights

- Near-instant vector search with **ObjectBox**
- Supports thousands of PDF pages with efficient chunking
- Uses **Groq's blazing-fast inference** for LLaMA3 model responses

---

## 🛡️ License

This project is licensed under the MIT License.

---


## 📞 Contact

For inquiries, collaborations, or support, reach out to:

**Garv Sharma**  
Email: garvsharma835@gmail.com  

---

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [ObjectBox Vector Database](https://objectbox.io/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [HuggingFace Transformers](https://huggingface.co/)

---


