# LLM Auto-Fuzzer (CS50x Capstone)

#### Video Demo: <TO FOLLOW>

## 📝 Description
The **LLM Auto-Fuzzer** is a specialised Red Teaming tool designed to evaluate the robustness of Large Language Models (LLMs) against prompt injection and obfuscation attacks. Unlike standard web applications, this project implements a **multi-language stack**, utilising **Python** for web orchestration and **C** for low-level string mutation.

---

## 🧠 Thinking Process & Background
This project is born from the intersection of professional experience and an insatiable curiosity for the future of Artificial Intelligence.

### The "Why"
As a professional with a background in **Banking and Fintech**, I have spent years navigating the rigorous security requirements of the financial world. My experience in **Red Teaming** taught me that the most dangerous vulnerabilities often hide in the "blind spots" of an application's logic. 

As the world shifts towards AI-driven infrastructure, I recognised a critical gap: **LLM safety is the new perimeter.** This project is my way of exploring that frontier—combining my foundation in traditional cybersecurity with the evolving challenges of AI Safety.

### Passion for the Future
I am deeply passionate about the cybersecurity landscape and am driven to be a part of the growing world of AI. My goal with this fuzzer is to demonstrate how low-level programming concepts (like those found in C) remain vital even in the era of high-level Generative AI. Whether it is through "Leetspeak" obfuscation or cross-lingual "Pivot Attacks," this tool is a testament to the belief that to secure AI, we must first learn how to break it ethically.

---

## 🏗️ Architecture & Design
This project was built with the philosophy that security tools should be both performant and accessible. The architecture is split into three distinct layers:

### 1. The Web Layer (Python & Flask)
The front-facing application handles user authentication, session management, and the coordination of the fuzzing pipeline. 
* **`app.py`**: Manages the routing logic and prevents unauthorised access via `@login_required`.
* **`helpers.py`**: Acts as the "bridge" between the web server, the OpenAI API, and the local C-Engine.

### 2. The Mutation Engine (C)
To demonstrate a mastery of low-level memory management and string manipulation (learnt in Weeks 1-5 of CS50x), a custom engine was developed in C. 
* **`core/engine.c`**: Performs high-speed text transformations including Base64 encoding, ROT13 rotation, and Leetspeak substitution.
* **`core/dictionary.h`**: Implements a German-language pivot attack, swapping English sensitive keywords for German equivalents to test cross-lingual safety filters.

### 3. The Data Layer (SQL)
All scan results, including the original prompt, the fuzzed payload, and the LLM's response, are stored in a relational SQLite database.
* **`schema.sql`**: Defines a relational structure that tracks "Severity Scores" calculated via Python's `match-case` logic.

---

## 🚀 Features
* **Automated Red Teaming:** Launch multiple mutation attacks against a single prompt with one click.
* **Severity Scoring:** An automated judge system that categorises LLM responses from "Safe/Refusal" to "Critical Bypass."
* **Hacker UI:** A dark-mode, terminal-inspired interface using Bootstrap and custom CSS.
* **Live Analytics:** A JavaScript-powered dashboard that visualises the success rates of different attack vectors.

---

## 🔧 Installation & Setup

To get the environment running on your local machine:

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Compile the C-Engine
cd core
make
cd ..

# 4. Initialise the Database
sqlite3 fuzzer.db < schema.sql

# 5. Run the Flask Server
flask run
