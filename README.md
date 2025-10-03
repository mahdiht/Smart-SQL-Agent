# 👕 T-Shirt Inventory Chatbot with LangChain & Streamlit

This project is an AI-powered chatbot that allows users to ask questions in natural language about a t-shirt inventory stored in a MySQL database. The chatbot automatically translates these questions into SQL queries using LangChain, and displays the answer—no SQL knowledge needed!

---

## 🚀 Features

- 💬 Ask natural language questions (e.g., *"How many red Nike shirts in size M?"*)
- 🤖 Automatic SQL generation using LangChain + LLM (LLaMA via Ollama)
- 🧠 Uses few-shot learning with semantic similarity to improve prompt quality
- 📊 SQL database with randomized t-shirt inventory and discounts
- 🖥️ Simple and interactive **Streamlit** web interface

---

## 🗂️ Project Structure

├── main.py # Streamlit UI for user interaction

├── Builder.py # Core logic: builds the LangChain SQL chain

├── few_shots.py # Few-shot examples to improve SQL generation

├── tshirt_db_creation.sql # SQL script to set up and populate the database

## Required packages include:

- streamlit

- langchain

- langchain-community

- langchain-experimental

- huggingface-hub

- chromadb

- pymysql

- sentence-transformers

- ollama

### Note: You must have Ollama installed and running a compatible model like llama3.

### 🎥 Demo Video

https://github.com/user-attachments/assets/65f32ad1-320d-4000-8383-9b265c5e325a

### SQL QUERY Verification:

<img width="490" height="156" alt="Image" src="https://github.com/user-attachments/assets/0772fa7f-7a52-43ad-8a63-aefd6f42d62a" />

### Answer verification using MySQL 

<img width="1155" height="587" alt="Capture d'écran 2025-10-03 104912" src="https://github.com/user-attachments/assets/dec35349-244e-48d8-928f-cf57c83fe985" />
