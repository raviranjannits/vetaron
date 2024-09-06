# Vetaron
It is an end-to-end website using **Generative AI** to answer queries related to animal problems.The website basically has a ChatBOT which works by using **RAG (Retrieval-Augmented Generation)** on an Encyclopaedia of animal disease , symptoms and its cure.

### TechStack:
* HuggingFace
* LangChain
* PineCone
* Flask
* Model Used = "mistralai/Mistral-7B-Instruct-v0.2"

## How to use the ChatBot
```cmd
git clone 
```
Go inside the Vetaron folder

```cmd
pip install -r requirements.txt
```

```cmd
python store_index.py
```
The above just needs to be run once


```cmd
python app.py
```
The above code needs to be run everytime you what to start your server and host it

Run **http://127.0.0.1:8080/** on any WebBrowser to enjoy the ChatBot
