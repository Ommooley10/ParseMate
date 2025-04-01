# ParseMate   

## **A Powerful LL(1) Grammar Checker for English Sentences**  

ParseMate is an **intelligent English grammar checker** that combines **LL(1) parsing, dependency analysis, and NLP techniques** to assess **syntactic correctness and grammatical accuracy**. It identifies **sentence structure issues, missing dependencies (such as subject-verb agreements and required prepositions), and grammatical errors** using a combination of **Context-Free Grammar (CFG) rules, NLP models, and AI-powered suggestions**.  

With an **interactive GUI**, ParseMate provides a **user-friendly experience** for real-time grammar checking.  

---

## **Why Use ParseMate?**  

 **Advanced Grammar Checking** – Uses **LL(1) parsing** to validate sentence structures.  
 **Dependency Analysis** – Ensures that sentences have **proper subject-verb agreement and necessary prepositions**.  
 **AI-Powered Suggestions** – Uses **LanguageTool** to identify spelling, grammatical, and stylistic errors.  
 **User-Friendly GUI** – Provides an **intuitive interface** using **Tkinter**.  
 **Lightweight & Fast** – Optimized for **quick sentence parsing and real-time grammar correction**.  

---

## **Tech Stack & Tools Used**  

ParseMate is built with **cutting-edge NLP and parsing technologies** to ensure accurate and efficient grammar checking.  

###  Python (Core Language) 🐍
Python is chosen as the **primary language** due to its:  
- **Rich ecosystem** for Natural Language Processing (NLP).  
- **Powerful libraries** that support machine learning and text analysis.  
- **Ease of integration** with GUI frameworks like Tkinter.  

###  spaCy (NLP Processing)   
- A fast and robust NLP library used for:  
  - **Tokenization** (breaking text into words).  
  - **Part-of-Speech (POS) tagging** (identifying nouns, verbs, adjectives, etc.).  
  - **Dependency parsing** (understanding relationships between words).  
- Helps dynamically extract **grammatical structures** from sentences.  

###  language-tool-python (Grammar Checking)   
- An AI-powered grammar checker used to:  
  - Detect **spelling mistakes, grammatical errors, and stylistic issues**.  
  - Provide **contextual suggestions** to improve sentence correctness.  
- It acts as a **secondary layer of validation** after LL(1) parsing.  

###  LL(1) Parsing (Context-Free Grammar)   
- A **top-down parsing algorithm** used for:  
  - Validating sentence structure **based on predefined grammar rules (CFG)**.  
  - Ensuring **syntactic correctness** by checking if a sentence conforms to **English syntax**.  
- Helps **detect structural errors** that AI-based checkers might miss.  

###  Tkinter (GUI Framework)   
- A **lightweight and built-in Python library** used to create the graphical user interface (GUI).  
- Enables users to **enter a sentence, check its grammar, and view detailed results** in an intuitive way.  
- Provides an interactive and **easy-to-use** experience.  

---

## **How to Run ParseMate?**   

###  Install Dependencies  
Install the required dependencies by running:  

```bash
pip install -r requirements.txt
```

###  If you encounter issues with spaCy models, install them manually: 

```bash
python -m spacy download en_core_web_sm
```

###  To launch the ParseMate application, run: 

```bash
python gui.py
```

---

##  The project is made by: 
### Om Mooley
### Madhuj Agrawal
