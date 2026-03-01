# 🌍 LingaTerminal

**LingaTerminal** is a Command-Line Interface (CLI) tool designed to bridge the language gap in technical education by translating programming commands into local dialects.

It transforms the terminal from a foreign technical interface into a familiar learning companion — enabling learners to understand programming concepts using their native language and culturally relevant analogies.

---

## 🚀 Project Vision

Modern programming ecosystems are heavily English-centric, creating barriers for students whose first language is not English.

LingaTerminal re-imagines the terminal as an **inclusive multilingual learning environment** by allowing users to:

- Explain programming commands in local languages
- Learn using culturally familiar analogies
- Understand terminal concepts intuitively
- Convert indigenous-language logic into valid programming code
- Learn programming without heavy reliance on internet access

The goal is to make technology feel **indigenous rather than imported**.

---

## 🎯 Problem Statement

Most programming documentation and tools are written in English. For many learners:

- English is a second or third language
- Technical terminology feels inaccessible
- Learning programming becomes unnecessarily difficult

This results in:

- Reduced participation in technology education
- Slower comprehension
- Psychological barriers to entry

**LingaTerminal addresses this challenge through linguistic inclusivity.**

---

## 🛠 Tech Stack

- **Python**
- **CLI Interface (Argparse)**
- **JSON-based Data Storage**
- **Modular Software Architecture**
- **Offline Translation Engine**

---

## 📂 Project Structure

linga_terminal/
│
├── main.py # Application entry point
├── config.py # Global configuration
│
├── cli/
│ ├── parser.py # CLI argument definitions
│ └── commands.py # Command handlers
│
├── services/
│ ├── translation_service.py
│ └── document_service.py
│
├── utils/
│ ├── file_handler.py
│ └── id_generator.py
│
└── data/
├── translations.json # Local dialect knowledge base
└── documents.json # Generated explanations


---

```bash
git clone <repo-url>
cd terminal_linga

python -m venv venv
source venv/bin/activate   # Linux / Mac
# venv\Scripts\activate    # Windows

pip install -r requirements.txt #Optional

# Explain a Terminal Command
python3 main.py explain --cmd "ls" --lang swahili

# Example Output:
Explanation:
Huonyesha faili ndani ya folda.

Analogy:
Ni kama kufungua droo kuona vilivyomo.

# Convert native-language logic into programming code:
python main.py transpile \
--code "ikiwa nambari ni kubwa kuliko 10 chapisha kubwa" \
--to python

# Example Output:
if number > 10:
    print("kubwa")